#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
티스토리 백업 파일을 옵시디언 제텔카스텐 노트로 변환하는 스크립트
작성자: Claude Code Assistant
목적: HTML 백업 파일을 마크다운 노트로 변환하여 제텔카스텐 구조에 통합
"""

import os
import re
from bs4 import BeautifulSoup
import html2text
from datetime import datetime
import shutil

class TistoryBackupConverter:
    def __init__(self, backup_path, obsidian_path):
        """
        초기화

        Args:
            backup_path (str): 티스토리 백업 파일 경로
            obsidian_path (str): 옵시디언 볼트 경로
        """
        self.backup_path = backup_path
        self.obsidian_path = obsidian_path
        self.output_dir = os.path.join(obsidian_path, "04-퍼블리싱", "티스토리-포스트")

        # HTML to Markdown 변환기 설정
        self.h = html2text.HTML2Text()
        self.h.ignore_links = False
        self.h.ignore_images = False
        self.h.body_width = 0
        self.h.ignore_emphasis = False
        self.h.ignore_tables = False

    def parse_html_file(self, html_file_path):
        """HTML 파일에서 메타데이터와 내용 추출"""
        try:
            with open(html_file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            soup = BeautifulSoup(content, 'html.parser')

            # 메타데이터 추출
            title_elem = soup.find('h2', class_='title-article')
            title = title_elem.get_text().strip() if title_elem else "제목 없음"

            category_elem = soup.find('p', class_='category')
            category = category_elem.get_text().strip() if category_elem else "기타"

            date_elem = soup.find('p', class_='date')
            date = date_elem.get_text().strip() if date_elem else ""

            # 본문 내용 추출
            content_elem = soup.find('div', class_='contents_style')
            if content_elem:
                # 이미지 경로 수정
                for img in content_elem.find_all('img'):
                    src = img.get('src', '')
                    if src.startswith('./img/'):
                        # 상대 경로를 절대 경로로 변경
                        folder_name = os.path.basename(os.path.dirname(html_file_path))
                        new_src = f"./img/{folder_name}_{os.path.basename(src)}"
                        img['src'] = new_src

                # HTML을 마크다운으로 변환
                html_content = str(content_elem)
                markdown_content = self.h.handle(html_content)
            else:
                markdown_content = ""

            return {
                'title': title,
                'category': category,
                'date': date,
                'content': markdown_content,
                'html_file': html_file_path
            }

        except Exception as e:
            print(f"HTML 파싱 실패 ({html_file_path}): {e}")
            return None

    def categorize_post(self, category, title):
        """실제 티스토리 카테고리에 기반한 포스트 분류"""

        # 실제 티스토리 카테고리 매핑
        tistory_category_mapping = {
            # 웹개발 & 프로그래밍
            'JavaScript': '웹개발-프로그래밍',
            'ReactJS': '웹개발-프로그래밍',
            'Python': '웹개발-프로그래밍',
            'Coding': '웹개발-프로그래밍',
            'PHP & MySQL': '웹개발-프로그래밍',
            '웹 표준의 정석': '웹개발-프로그래밍',
            '비전공자를 위한 IT지식': '웹개발-프로그래밍',

            # AI & 딥러닝
            '밑바닥부터 시작하는 딥러닝': 'AI-딥러닝',
            '생성형 AI를 활용한 서비스 콘텐츠 제작': 'AI-딥러닝',

            # 보안 & 해킹
            'Dreamhack': '보안-해킹',
            '워게임': '보안-해킹',
            'CTF': '보안-해킹',

            # 자격증 & 교육
            '자격증': '자격증-교육',
            '[K-Shield 주니어] 기초과정 11차 교육': '자격증-교육',
            '[2025년 7월 교육] NAVER CLOUD PLATFORM AI Ha': '자격증-교육',

            # 세미나 & 컨퍼런스
            '세미나,컴퍼런스,강의': '세미나-컨퍼런스',

            # 외부활동 & 국제
            '대외활동': '외부활동',
            '2025 제 7기 미국알기 아카데미': '외부활동',
            '국제': '외부활동'
        }

        # 키워드 기반 매핑 (카테고리와 제목 모두 체크)
        keyword_mapping = {
            # 웹개발 & 프로그래밍
            'javascript': '웹개발-프로그래밍',
            'react': '웹개발-프로그래밍',
            'python': '웹개발-프로그래밍',
            'coding': '웹개발-프로그래밍',
            'php': '웹개발-프로그래밍',
            'mysql': '웹개발-프로그래밍',
            'html': '웹개발-프로그래밍',
            'css': '웹개발-프로그래밍',
            '웹': '웹개발-프로그래밍',
            '프로그래밍': '웹개발-프로그래밍',

            # AI & 딥러닝
            'ai': 'AI-딥러닝',
            '딥러닝': 'AI-딥러닝',
            'deep': 'AI-딥러닝',
            'learning': 'AI-딥러닝',
            'lstm': 'AI-딥러닝',
            'cnn': 'AI-딥러닝',
            'rnn': 'AI-딥러닝',
            'gpt': 'AI-딥러닝',
            'langchain': 'AI-딥러닝',
            'gemini': 'AI-딥러닝',
            '인공지능': 'AI-딥러닝',
            '머신러닝': 'AI-딥러닝',
            'mnist': 'AI-딥러닝',
            'numpy': 'AI-딥러닝',

            # 보안 & 해킹
            'dreamhack': '보안-해킹',
            '워게임': '보안-해킹',
            'ctf': '보안-해킹',
            '해킹': '보안-해킹',
            '보안': '보안-해킹',
            '침투': '보안-해킹',
            '노말틱': '보안-해킹',

            # 자격증 & 교육
            '자격증': '자격증-교육',
            'aice': '자격증-교육',
            'naver': '자격증-교육',
            'cloud': '자격증-교육',
            'k-shield': '자격증-교육',
            '교육': '자격증-교육',

            # 세미나 & 컨퍼런스
            '세미나': '세미나-컨퍼런스',
            '컨퍼런스': '세미나-컨퍼런스',
            '강의': '세미나-컨퍼런스',
            'expo': '세미나-컨퍼런스',
            '메타콘': '세미나-컨퍼런스',

            # 외부활동
            '대외활동': '외부활동',
            '미국알기': '외부활동',
            '아카데미': '외부활동',
            '해커톤': '외부활동',

            # 대학수업 & 이론
            '수치최적화': '대학수업-이론',
            '데이터 사이언스': '대학수업-이론',
            '최적화이론': '대학수업-이론',
            '학기': '대학수업-이론',
            '국가': '대학수업-이론',
            '안보': '대학수업-이론'
        }

        # 1. 먼저 정확한 티스토리 카테고리 매칭 시도
        if category in tistory_category_mapping:
            return tistory_category_mapping[category]

        # 2. 키워드 기반 매칭
        text_to_check = f"{category} {title}".lower()

        for keyword, folder in keyword_mapping.items():
            if keyword in text_to_check:
                return folder

        # 3. 기본값
        return '기타'

    def sanitize_filename(self, title):
        """파일명에서 특수문자 제거"""
        # 윈도우에서 사용할 수 없는 문자 제거
        invalid_chars = '<>:"/\\|?*'
        for char in invalid_chars:
            title = title.replace(char, '')

        # 길이 제한
        title = title[:100] if len(title) > 100 else title
        return title.strip()

    def copy_images(self, source_folder, post_id, target_folder):
        """이미지 파일들을 대상 폴더로 복사"""
        img_source = os.path.join(source_folder, 'img')
        if not os.path.exists(img_source):
            return []

        img_target = os.path.join(target_folder, 'img')
        os.makedirs(img_target, exist_ok=True)

        copied_files = []
        for file in os.listdir(img_source):
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                source_file = os.path.join(img_source, file)
                # 파일명에 포스트 ID 접두사 추가
                target_file = os.path.join(img_target, f"{post_id}_{file}")
                shutil.copy2(source_file, target_file)
                copied_files.append(f"{post_id}_{file}")

        return copied_files

    def create_obsidian_note(self, post_data, post_id):
        """옵시디언 노트 형식으로 변환"""
        title = post_data['title']
        safe_title = self.sanitize_filename(title)
        category_folder = self.categorize_post(post_data['category'], title)

        # 폴더 생성
        folder_path = os.path.join(self.output_dir, category_folder)
        os.makedirs(folder_path, exist_ok=True)

        # 이미지 복사
        source_folder = os.path.dirname(post_data['html_file'])
        copied_images = self.copy_images(source_folder, post_id, folder_path)

        # 마크다운 내용에서 이미지 경로 수정
        content = post_data['content']
        for img_file in copied_images:
            old_path = f"./img/{img_file.replace(f'{post_id}_', '')}"
            new_path = f"./img/{img_file}"
            content = content.replace(old_path, new_path)

        # 파일 경로
        file_path = os.path.join(folder_path, f"{safe_title}.md")

        # 노트 내용 구성
        note_content = f"""# {title}

> **원본 포스트 ID**: {post_id}
> **발행일**: {post_data['date']}
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

**태그**: #{post_data['category'].replace(' ', '').replace('/', '')}
**상태**: 🌱 씨앗 (제텔카스텐 통합 대기)
**변환일**: {datetime.now().strftime('%Y-%m-%d')}
"""

        # 파일 저장
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(note_content)
            print(f"생성됨: {safe_title}")
            return file_path
        except Exception as e:
            print(f"파일 저장 실패: {e}")
            return None

    def convert_all_posts(self):
        """모든 백업 포스트를 변환"""
        print(f"티스토리 백업 변환 시작...")
        print(f"백업 경로: {self.backup_path}")
        print(f"저장 경로: {self.output_dir}")

        if not os.path.exists(self.backup_path):
            print("백업 경로를 찾을 수 없습니다.")
            return

        success_count = 0
        total_count = 0

        # 숫자로 된 폴더들을 찾기
        for folder_name in os.listdir(self.backup_path):
            folder_path = os.path.join(self.backup_path, folder_name)

            if not os.path.isdir(folder_path):
                continue

            if not folder_name.isdigit():
                continue

            # HTML 파일 찾기
            html_files = [f for f in os.listdir(folder_path) if f.endswith('.html')]

            for html_file in html_files:
                html_file_path = os.path.join(folder_path, html_file)
                total_count += 1

                print(f"\n[{total_count}] 처리 중: {html_file}")

                # HTML 파싱
                post_data = self.parse_html_file(html_file_path)
                if not post_data:
                    print("HTML 파싱 실패")
                    continue

                # 이미 존재하는지 확인
                safe_title = self.sanitize_filename(post_data['title'])
                if self.is_note_exists(safe_title):
                    print(f"이미 존재함: {safe_title}")
                    continue

                # 옵시디언 노트 생성
                file_path = self.create_obsidian_note(post_data, folder_name)
                if file_path:
                    success_count += 1

        print(f"\n변환 완료: {success_count}/{total_count}개 성공")

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
    BACKUP_PATH = r"C:\Users\박성호꺼\Desktop\idea4322-1-1"
    OBSIDIAN_PATH = r"C:\Users\박성호꺼\Desktop\옵시디언"

    # 변환 실행
    converter = TistoryBackupConverter(BACKUP_PATH, OBSIDIAN_PATH)
    converter.convert_all_posts()

if __name__ == "__main__":
    main()