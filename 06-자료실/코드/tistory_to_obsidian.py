#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
티스토리 블로그 포스트를 옵시디언 노트로 자동 변환하는 스크립트
작성자: Claude Code Assistant
목적: RSS 피드를 통해 티스토리 포스트를 마크다운 노트로 변환
"""

import feedparser
import requests
from bs4 import BeautifulSoup
import os
import re
from datetime import datetime
import html2text
from urllib.parse import urlparse
import time

class TistoryToObsidian:
    def __init__(self, blog_url, obsidian_path):
        """
        초기화

        Args:
            blog_url (str): 티스토리 블로그 URL (예: "https://idea4322.tistory.com")
            obsidian_path (str): 옵시디언 볼트 경로
        """
        self.blog_url = blog_url.rstrip('/')
        self.rss_url = f"{blog_url}/rss"
        self.obsidian_path = obsidian_path
        self.output_dir = os.path.join(obsidian_path, "04-퍼블리싱", "티스토리-포스트")

        # HTML to Markdown 변환기 설정
        self.h = html2text.HTML2Text()
        self.h.ignore_links = False
        self.h.ignore_images = False
        self.h.body_width = 0  # 줄바꿈 제한 없음

    def fetch_rss_posts(self, limit=10):
        """RSS 피드에서 포스트 목록 가져오기"""
        try:
            feed = feedparser.parse(self.rss_url)
            posts = []

            for entry in feed.entries[:limit]:
                post_data = {
                    'title': entry.title,
                    'link': entry.link,
                    'published': entry.published if hasattr(entry, 'published') else '',
                    'summary': entry.summary if hasattr(entry, 'summary') else '',
                    'category': self.extract_category(entry)
                }
                posts.append(post_data)

            return posts
        except Exception as e:
            print(f"RSS 피드 읽기 실패: {e}")
            return []

    def extract_category(self, entry):
        """포스트 카테고리 추출"""
        if hasattr(entry, 'tags') and entry.tags:
            return entry.tags[0].term
        elif hasattr(entry, 'category'):
            return entry.category
        else:
            return "기타"

    def fetch_post_content(self, post_url):
        """개별 포스트의 전체 내용 가져오기"""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(post_url, headers=headers)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')

            # 티스토리 포스트 본문 추출 (일반적인 클래스명들)
            content_selectors = [
                '.article_view',
                '.entry-content',
                '.post-content',
                '.tt_article_useless_p_margin',
                'div[data-ke-type="content"]'
            ]

            content = None
            for selector in content_selectors:
                content = soup.select_one(selector)
                if content:
                    break

            if not content:
                # 대안: body에서 주요 콘텐츠 추출
                content = soup.find('body')

            return content.get_text() if content else ""

        except Exception as e:
            print(f"포스트 내용 가져오기 실패 ({post_url}): {e}")
            return ""

    def sanitize_filename(self, title):
        """파일명에서 특수문자 제거"""
        # 윈도우에서 사용할 수 없는 문자 제거
        invalid_chars = '<>:"/\\|?*'
        for char in invalid_chars:
            title = title.replace(char, '')

        # 길이 제한
        title = title[:100] if len(title) > 100 else title
        return title.strip()

    def categorize_post(self, category, title):
        """포스트를 적절한 폴더로 분류"""
        category_mapping = {
            'AI': '웹개발-AI',
            'GPT': '웹개발-AI',
            'LLM': '웹개발-AI',
            '웹개발': '웹개발-AI',
            '해킹': '해킹학습',
            '보안': '해킹학습',
            'security': '해킹학습',
            '학습': '추가학습',
            '강의': '추가학습',
            '대학': '대학수업',
            '세미나': '세미나-컨퍼런스',
            '컨퍼런스': '세미나-컨퍼런스',
            '자격증': '자격증',
            '외부': '외부활동'
        }

        # 카테고리나 제목에서 키워드 매칭
        for keyword, folder in category_mapping.items():
            if keyword.lower() in category.lower() or keyword.lower() in title.lower():
                return folder

        return '기타'  # 기본 폴더

    def create_obsidian_note(self, post_data, content):
        """옵시디언 노트 형식으로 변환"""
        title = post_data['title']
        safe_title = self.sanitize_filename(title)
        category_folder = self.categorize_post(post_data['category'], title)

        # 폴더 생성
        folder_path = os.path.join(self.output_dir, category_folder)
        os.makedirs(folder_path, exist_ok=True)

        # 파일 경로
        file_path = os.path.join(folder_path, f"{safe_title}.md")

        # 노트 내용 구성
        note_content = f"""# {title}

> **원문**: {post_data['link']}
> **발행일**: {post_data['published']}
> **카테고리**: {post_data['category']}

## 📝 원문 내용

{content}

## 🔗 제텔카스텐 연결

### 관련 개념
- [[]]
- [[]]

### 프로젝트 연결
- [[]]

### 학습 포인트
-

## 📋 액션 아이템
- [ ]
- [ ]

## 💡 개인적 통찰


---

**태그**: #{post_data['category'].replace(' ', '')}
**상태**: 🌱 씨앗 (제텔카스텐 통합 대기)
**마지막 수정**: {datetime.now().strftime('%Y-%m-%d')}
"""

        # 파일 저장
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(note_content)
            print(f"✅ 생성됨: {safe_title}")
            return file_path
        except Exception as e:
            print(f"❌ 파일 저장 실패: {e}")
            return None

    def sync_posts(self, limit=5):
        """전체 동기화 실행"""
        print(f"🔄 티스토리 포스트 동기화 시작...")
        print(f"📍 블로그: {self.blog_url}")
        print(f"📁 저장 경로: {self.output_dir}")

        # RSS 포스트 가져오기
        posts = self.fetch_rss_posts(limit)
        if not posts:
            print("❌ RSS 피드에서 포스트를 가져올 수 없습니다.")
            return

        print(f"📄 총 {len(posts)}개 포스트 발견")

        success_count = 0
        for i, post in enumerate(posts, 1):
            print(f"\n[{i}/{len(posts)}] 처리 중: {post['title'][:50]}...")

            # 이미 존재하는지 확인
            safe_title = self.sanitize_filename(post['title'])
            if self.is_note_exists(safe_title):
                print(f"⏭️ 이미 존재함: {safe_title}")
                continue

            # 포스트 내용 가져오기
            content = self.fetch_post_content(post['link'])
            if not content:
                print("❌ 내용 가져오기 실패")
                continue

            # 옵시디언 노트 생성
            file_path = self.create_obsidian_note(post, content)
            if file_path:
                success_count += 1

            # 요청 간격 (서버 부하 방지)
            time.sleep(1)

        print(f"\n🎉 동기화 완료: {success_count}/{len(posts)}개 성공")

    def is_note_exists(self, title):
        """노트가 이미 존재하는지 확인"""
        for root, dirs, files in os.walk(self.output_dir):
            for file in files:
                if file.startswith(title) and file.endswith('.md'):
                    return True
        return False

def main():
    """메인 실행 함수"""
    # 설정
    BLOG_URL = "https://idea4322.tistory.com"
    OBSIDIAN_PATH = r"C:\Users\박성호꺼\Desktop\옵시디언"

    # 동기화 실행
    sync = TistoryToObsidian(BLOG_URL, OBSIDIAN_PATH)
    sync.sync_posts(limit=10)  # 최신 10개 포스트

if __name__ == "__main__":
    main()