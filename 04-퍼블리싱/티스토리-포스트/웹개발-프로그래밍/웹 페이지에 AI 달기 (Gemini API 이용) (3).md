# 웹 페이지에 AI 달기 (Gemini API 이용) (3)

> **원본 포스트 ID**: 220
> **발행일**: 2025-07-15 15:54:38
> **카테고리**: project/웹개발

## 📝 원문 내용

이번엔 API를 Vercel에 숨겨서 백엔드에서 꺼내와서 보안을 신경 써보겠다.

** Node.js 설치하기 **

<https://nodejs.org/ko>

[ Node.js — Run JavaScript Everywhere Node.js® is a free, open-source, cross-platform JavaScript runtime environment that lets developers create servers, web apps, command line tools and scripts. nodejs.org ](https://nodejs.org/ko)

**Vercel CLI 설치**

Vercel CLI는 개발자의 터미널에서 Vercel 플랫폼의 기능을 직접 제어하기 위한 공식 명령어 도구이다. 

이를 통해 로컬에서 클라우드 환경을 모방하여 테스트하고, 명령 한 줄로 프로젝트를 전 세계에 배포할 수 있다.
    
    
    npm install -g vercel

**script.js 수정**
    
    
    function ask(){
    
        let requestBody = {
            contents:history
        };
    
        let apikey = apikeyInput.value;
        let url = "/api/gemini"
        let request = {
        method:"POST",
        headers:{
            "Content-Type":"application/json",
        },
        body: JSON.stringify(requestBody)
        };
    
        fetch(url, request)
        .then(function(response){ return response.json() })
        .then(function(data){
    
          console.log(data);
            let message = data.candidates[0].content.parts[0].text
            addMessage(message,"model");
        })
    }

js파일을 하나 더 만든다음 백엔드 역할을 하게 합니다.

api/gemini.js
    
    
    // Vercel 서버리스 함수는 반드시 'export default'로 함수를 내보내야 합니다.
    // 이 함수는 두 개의 인자(req, res)를 받습니다.
    
    export default function handler(req, res) {
    
      // 환경변수에서 API 키 가져오기
      let apikey = process.env.GEMINI_API_KEY;
      // Gemini API URL
      let url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent';
    
      // Gemini API 호출
    	fetch(url, {
    	  method: "POST",
    	  headers: {
    	    "Content-Type": "application/json",
    	    "X-goog-api-key": apikey
    	  },
        body: JSON.stringify(req.body)
      })
      .then(response => response.json())
      .then(data => {
    
        // 응답 데이터 반환
        res.json(data);
      })
      
    }

.env
    
    
    GEMINI_API_KEY=#Gemini API Key 여기에 삽입

이제 <https://vercel.com/>

[ Vercel: Build and deploy the best web experiences with the AI Cloud – Vercel Vercel gives developers the frameworks, workflows, and infrastructure to build a faster, more personalized web. vercel.com ](https://vercel.com/)

![](./img/220_img.png)

Settings

![](./img/220_img_1.png)

저기 Key에 자신의 API key를 넣으면 된다.

최종 배포 버전

<https://ai-chat-vercel-git-main-pk42acs-projects.vercel.app/>

[ 인공지능 채팅 ai-chat-vercel-git-main-pk42acs-projects.vercel.app ](https://ai-chat-vercel-git-main-pk42acs-projects.vercel.app/)


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

**태그**: #project웹개발
**상태**: 🌱 씨앗 (제텔카스텐 통합 대기)
**변환일**: 2025-10-07
