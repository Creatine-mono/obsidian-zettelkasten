#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
티스토리 포스트를 실제 카테고리에 맞춰 재분류하는 스크립트
"""

import os
import shutil
import re

def get_post_category_from_content(file_path):
    """파일 내용을 읽어서 원본 카테고리 정보 추출"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 카테고리 정보 추출
        category_match = re.search(r'> \*\*카테고리\*\*: (.+)', content)
        if category_match:
            return category_match.group(1)
        return None
    except:
        return None

def categorize_by_tistory_categories(category, title):
    """실제 티스토리 카테고리 기반 분류"""

    # 키워드 기반 매핑
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
        '개발자': '웹개발-프로그래밍',
        'git': '웹개발-프로그래밍',
        '커밋': '웹개발-프로그래밍',
        '브랜치': '웹개발-프로그래밍',
        '프레임워크': '웹개발-프로그래밍',
        '라이브러리': '웹개발-프로그래밍',

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
        '신경망': 'AI-딥러닝',
        '합성곱': 'AI-딥러닝',
        '순환': 'AI-딥러닝',
        '손글씨': 'AI-딥러닝',
        '다중': 'AI-딥러닝',
        '분류': 'AI-딥러닝',
        '회귀': 'AI-딥러닝',

        # 보안 & 해킹
        'dreamhack': '보안-해킹',
        '워게임': '보안-해킹',
        'ctf': '보안-해킹',
        '해킹': '보안-해킹',
        '보안': '보안-해킹',
        '침투': '보안-해킹',
        '노말틱': '보안-해킹',
        '취업반': '보안-해킹',
        '스터디': '보안-해킹',
        '모의': '보안-해킹',

        # 자격증 & 교육
        '자격증': '자격증-교육',
        'aice': '자격증-교육',
        'naver': '자격증-교육',
        'cloud': '자격증-교육',
        'k-shield': '자격증-교육',
        '교육': '자격증-교육',
        '케이쉴드': '자격증-교육',
        '수료': '자격증-교육',
        '합격': '자격증-교육',
        'aws': '자격증-교육',

        # 세미나 & 컨퍼런스
        '세미나': '세미나-컨퍼런스',
        '컨퍼런스': '세미나-컨퍼런스',
        '강의': '세미나-컨퍼런스',
        'expo': '세미나-컨퍼런스',
        '메타콘': '세미나-컨퍼런스',
        '메타위크': '세미나-컨퍼런스',

        # 외부활동
        '대외활동': '외부활동',
        '미국알기': '외부활동',
        '아카데미': '외부활동',
        '해커톤': '외부활동',
        'kisia': '외부활동',

        # 대학수업 & 이론
        '수치최적화': '대학수업-이론',
        '데이터 사이언스': '대학수업-이론',
        '최적화이론': '대학수업-이론',
        '학기': '대학수업-이론',
        '국가': '대학수업-이론',
        '안보': '대학수업-이론',
        '개인정보': '대학수업-이론',
        '경사': '대학수업-이론',
        '하강법': '대학수업-이론',
        '선형': '대학수업-이론',
        '근사': '대학수업-이론',
        '내적': '대학수업-이론'
    }

    # 키워드 기반 매칭
    text_to_check = f"{category} {title}".lower()

    for keyword, folder in keyword_mapping.items():
        if keyword in text_to_check:
            return folder

    return '기타'

def reorganize_posts():
    """포스트 재분류 실행"""
    base_path = r"C:\Users\박성호꺼\Desktop\옵시디언\04-퍼블리싱\티스토리-포스트"

    # 기존 폴더들
    old_folders = ['웹개발-AI', '해킹학습', '추가학습', '기타', '대학수업', '자격증', '세미나-컨퍼런스', '외부활동']

    # 새 폴더 구조
    new_folders = ['웹개발-프로그래밍', 'AI-딥러닝', '보안-해킹', '자격증-교육', '대학수업-이론', '세미나-컨퍼런스', '외부활동', '기타']

    # 새 폴더 생성
    for folder in new_folders:
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        # img 폴더도 생성
        img_path = os.path.join(folder_path, 'img')
        os.makedirs(img_path, exist_ok=True)

    moved_count = 0
    total_count = 0

    # 각 기존 폴더에서 파일들을 새 위치로 이동
    for old_folder in old_folders:
        old_folder_path = os.path.join(base_path, old_folder)

        if not os.path.exists(old_folder_path):
            continue

        # 마크다운 파일들 처리
        for file in os.listdir(old_folder_path):
            if file.endswith('.md'):
                file_path = os.path.join(old_folder_path, file)
                total_count += 1

                # 파일에서 카테고리 정보 추출
                category = get_post_category_from_content(file_path)
                title = file.replace('.md', '')

                # 새 카테고리 결정
                new_category = categorize_by_tistory_categories(category or '', title)

                # 새 위치로 이동
                new_folder_path = os.path.join(base_path, new_category)
                new_file_path = os.path.join(new_folder_path, file)

                if file_path != new_file_path:
                    try:
                        shutil.move(file_path, new_file_path)
                        moved_count += 1
                        print(f"이동: {file} -> {new_category}")
                    except Exception as e:
                        print(f"이동 실패: {file} - {e}")

        # img 폴더 내용 이동
        old_img_path = os.path.join(old_folder_path, 'img')
        if os.path.exists(old_img_path):
            for img_file in os.listdir(old_img_path):
                old_img_file_path = os.path.join(old_img_path, img_file)

                # 이미지 파일명에서 포스트 ID 추출하여 해당 마크다운 파일 찾기
                post_id = img_file.split('_')[0]

                # 해당 포스트가 어느 카테고리로 이동했는지 찾기
                target_category = None
                for new_folder in new_folders:
                    new_folder_path = os.path.join(base_path, new_folder)
                    for md_file in os.listdir(new_folder_path):
                        if md_file.endswith('.md'):
                            md_content = get_post_category_from_content(os.path.join(new_folder_path, md_file))
                            if post_id in md_file or (md_content and post_id in md_content):
                                target_category = new_folder
                                break
                    if target_category:
                        break

                if target_category:
                    new_img_path = os.path.join(base_path, target_category, 'img', img_file)
                    try:
                        shutil.move(old_img_file_path, new_img_path)
                        print(f"이미지 이동: {img_file} -> {target_category}")
                    except Exception as e:
                        print(f"이미지 이동 실패: {img_file} - {e}")

    print(f"\n재분류 완료: {moved_count}/{total_count}개 파일 이동")

    # 빈 폴더 제거
    for old_folder in old_folders:
        old_folder_path = os.path.join(base_path, old_folder)
        try:
            if os.path.exists(old_folder_path) and not os.listdir(old_folder_path):
                os.rmdir(old_folder_path)
                print(f"빈 폴더 제거: {old_folder}")
        except:
            pass

if __name__ == "__main__":
    reorganize_posts()