# 📖 옵시디언-GitHub 연동 설정 가이드

> 제텔카스텐 노트를 GitHub에 자동 백업하여 안전하게 보관하고 버전 관리하기

## 🎯 목표
- 옵시디언 노트 변경사항 자동 GitHub 백업
- 버전 관리를 통한 변경 이력 추적
- 여러 기기 간 동기화
- 데이터 손실 방지

## 🔧 방법 1: Obsidian Git 플러그인 (추천)

### 1단계: 플러그인 설치
1. 옵시디언에서 `설정(⚙️)` → `커뮤니티 플러그인` 이동
2. `브라우저` 클릭 → "Obsidian Git" 검색
3. 설치 후 활성화

### 2단계: GitHub Repository 생성
```bash
# GitHub에서 새 레포지토리 생성
Repository name: obsidian-zettelkasten
Description: 제텔카스텐 지식 관리 시스템
✅ Private (개인정보 보호)
✅ Add README file
```

### 3단계: 로컬 Git 초기화
```bash
# 옵시디언 볼트 폴더에서 실행
cd "C:\Users\박성호꺼\Desktop\옵시디언"

# Git 초기화
git init

# GitHub 저장소 연결
git remote add origin https://github.com/[당신의계정]/obsidian-zettelkasten.git

# 첫 커밋
git add .
git commit -m "Initial commit: 제텔카스텐 시스템 구축 완료"
git branch -M main
git push -u origin main
```

### 4단계: Obsidian Git 설정
```
플러그인 설정에서:
- Auto-pull interval: 10분
- Auto-push interval: 10분
- Auto-backup after file change: ON
- Commit message: "vault backup: {{date}}"
```

## 🔧 방법 2: GitHub Desktop 사용

### 1단계: GitHub Desktop 설치
- [GitHub Desktop](https://desktop.github.com/) 다운로드 설치

### 2단계: 저장소 생성
1. GitHub Desktop에서 `File` → `New Repository`
2. Name: `obsidian-zettelkasten`
3. Local path: `C:\Users\박성호꺼\Desktop\옵시디언`
4. Initialize with README: ✅

### 3단계: .gitignore 설정
```gitignore
# 옵시디언 캐시 파일 제외
.obsidian/workspace.json
.obsidian/cache
.obsidian/plugins/*/data.json
.trash/

# 개인정보 관련 파일 제외
*.tmp
*.log
```

## 📋 권장 워크플로우

### 일상적 사용
```
1. 옵시디언에서 노트 작성/수정
2. Obsidian Git 플러그인이 자동으로 10분마다 백업
3. 수동 동기화 필요시: Ctrl+P → "Obsidian Git: Create backup"
```

### 수동 백업 (필요시)
```bash
# 중요한 변경사항 즉시 백업
git add .
git commit -m "중요 업데이트: [변경 내용 설명]"
git push
```

## ⚠️ 주의사항

### 개인정보 보호
- **Private Repository** 필수 사용
- API 키, 비밀번호 등 민감 정보 제외
- `.gitignore`로 개인 설정 파일 제외

### 파일 크기 제한
- GitHub 파일당 100MB 제한
- 대용량 이미지/PDF는 별도 관리 고려
- Git LFS 사용 검토 (필요시)

### 동기화 충돌 방지
```
권장사항:
- 한 번에 한 기기에서만 작업
- 작업 전 항상 최신 버전 pull
- 충돌 발생시 Obsidian Git이 자동 해결
```

## 🚀 추가 기능들

### 브랜치 활용
```bash
# 실험적 노트 작성용 브랜치
git checkout -b experiment-notes

# 완료 후 메인 브랜치에 병합
git checkout main
git merge experiment-notes
```

### 특정 폴더만 백업
```gitignore
# .gitignore에 추가하여 특정 폴더 제외
07-아카이브/
temp/
drafts/
```

### 자동화 스크립트
```bash
# backup.bat 파일 생성 (Windows)
@echo off
cd "C:\Users\박성호꺼\Desktop\옵시디언"
git add .
git commit -m "Auto backup: %date% %time%"
git push
echo Backup completed!
pause
```

## 📊 백업 상태 확인

### Git 상태 확인
```bash
git status          # 변경사항 확인
git log --oneline   # 커밋 이력 확인
git remote -v       # 원격 저장소 확인
```

### GitHub에서 확인
- Repository 페이지에서 최근 커밋 확인
- 파일 변경 이력 추적
- 이슈/토론 기능 활용 가능

## 🎯 완료 후 혜택

### 1. 데이터 안전성
- 클라우드 백업으로 데이터 손실 방지
- 버전 관리로 이전 상태 복구 가능

### 2. 협업 가능성
- 팀 프로젝트 시 지식 공유
- 코드 리뷰처럼 노트 리뷰 가능

### 3. 포트폴리오 가치
- GitHub 활동으로 학습 의지 어필
- 체계적인 지식 관리 능력 증명

---

**다음 단계**: Obsidian Git 플러그인 설치 후 첫 백업 테스트
**예상 소요 시간**: 30분
**난이도**: ⭐⭐⭐☆☆

**Tags**: #GitHub연동 #자동백업 #버전관리 #옵시디언설정