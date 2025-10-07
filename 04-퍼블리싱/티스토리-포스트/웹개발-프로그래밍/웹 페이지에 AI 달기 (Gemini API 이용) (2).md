# 웹 페이지에 AI 달기 (Gemini API 이용) (2)

> **원본 포스트 ID**: 219
> **발행일**: 2025-07-15 15:43:18
> **카테고리**: project/웹개발

## 📝 원문 내용

** 채팅 UI 와 기본 챗봇 만들기 **

채팅 UI 구성하기

index.html
    
    
      <main>
        <!-- 메시지가 표시될 컨테이너 -->
        <div id="messages"></div>
    
        <!-- 사용자 입력 UI -->
        <div id="input-container">
          <input type="text" id="input" placeholder="메시지 입력">
          <button id="button">전송</button>
        </div>
      </main>

script.js

메세지 박스 추가하기
    
    
    // 메시지를 화면에 추가하는 함수 (role 매개변수에 따라 다른 클래스 적용)
    function addMessage(message, role) {
      let messageElement = document.createElement("div"); // 새로운 메시지 요소 생성
      messageElement.textContent = message;               // 메시지 텍스트 설정
      
      messageElement.classList.add(role); // role 매개변수를 그대로 CSS 클래스명으로 사용
      
      messagebox.append(messageElement);          // 메시지 컨테이너에 추가
      
      // 스크롤을 최하단으로 이동
      messagebox.scrollTop = messagebox.scrollHeight;
    }
    
    
    // DOM 요소 선택
    let messagebox = document.querySelector("#messages");
    let input = document.querySelector("#input");
    let button = document.querySelector("#button");
    
    // 전송 버튼 클릭 이벤트 처리
    button.addEventListener("click", function() {
      let message = input.value;    // 입력창 값 가져오기
      
      addMessage(message, "user");  // 사용자 메시지 표시
      input.value = "";             // 입력창 비우기
    })
    
    // 엔터 키 입력 처리 - 전송버튼 클릭과 동일한 효과
    input.addEventListener("keypress", function(event) {
    	// 엔터키 입력시 전송버튼 클릭
      if (event.key === "Enter") {
        button.click();
      }
    })

**Gemini API 응답 받기 **
    
    
    ask(message){
    
    	let apikey = 'GEMINI_API_KEY';
    	let url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent';
    	
    	fetch(url, {
    	  method: "POST",
    	  headers: {
    	    "Content-Type": "application/json",
    	    "X-goog-api-key": apikey
    	  },
    	  body: JSON.stringify({
    	    contents: [{
    	      parts: [{ text: message }]
    	    }]
    	  })
    	})
    	.then(function(response){ return response.json() })
    	.then(function(data){
    	  console.log(data); // API 응답 결과
    	  let message = data.candidates[0].content.parts[0].text;
    	  addMessage(message, "model");
    	})
    	.catch(error => {
    	  console.error("API 호출 오류:", error); // 필수는 아님
    	});
    	
    }
    
    
    // 전송 버튼 클릭 이벤트 처리
    button.addEventListener("click", function() {
      let message = input.value;
      
      addMessage(message, "user");
      ask(message);                // 유저메세지 박스생성후 Gemini API 요청
      input.value = "";
    })

여기까지만 하면 대화 맥락을 이해를 못한다 기억을 하게 해보자
    
    
    // 대화내용을 저장할 배열
    let history = [];
    
    
    addMessage(message, role){
    
    	// history 배열에 메세지 저장
    	history.push({
    	    role: role,
    	    parts: [{ text: message }]
    	});
    	
    	/* 나머지 코드 ... */
    	
    }
    
    
    fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        contents: history   // 대화내용으로 history를 전달한다
      })
    })

**대화내역 저장갯수 제한**
    
    
    // 대화 기록이 너무 길어지면 오래된 메시지 제거 (API 한도 고려)
    if (history.length > 20) {
      history = history.slice(history.length - 20);
    }

**API 키 입력창 만들기 : API키 입력칸을 만들면 백엔드에 API를 숨기지 않아도 된다.**
    
    
    let apikeyInput = document.querySelector("#apikey");
    
    // 로컬 스토리지에서 API 키 불러오기
    let apikey = localStorage.getItem("apikey");
    
    // 저장된 API 키가 있으면 입력란에 설정
    if(apikey){
      apikeyInput.value = apikey;
    }
    
    // API 키 변경 시 로컬 스토리지에 저장
    apikeyInput.addEventListener("change", function(event) {
      localStorage.setItem("apikey", apikeyInput.value);
    })
    
    // Gemini API에 메시지를 보내고 응답을 받는 함수
    function ask(message){
      let apikey = apikeyInput.value;  // API 입력창에서 값을 받아온다

**System Instruction 추가하기 **
    
    
    {
      contents: conversationHistory,
      systemInstruction: {
        parts: [{ text: "너는 중세 시대의 마법사이다. 역할에 맞는 말투로 응답해" }]
      }
    }
    
    
    function convertToStrong(text) {
      // '**'로 시작하고 끝나는 모든 문자열을 찾아 '<strong>' 태그로 감싸줍니다.
      // / \*\* (.*?) \*\* /g 라는 정규 표현식을 사용합니다.
      // (.*?) : ** 와 ** 사이의 모든 문자(줄바꿈 제외)를 찾습니다. '?'는 가장 짧은 일치를 찾게 합니다(non-greedy).
      // g : 문자열 전체에서 일치하는 모든 부분을 찾도록 하는 플래그입니다.
      // $1 : 정규식의 첫 번째 괄호 그룹에서 캡처된 텍스트를 의미합니다.
      return text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    }

**완성된 AI Chat 웹페이지**

<https://aichat-gemini-api-main.vercel.app/>

[ AI Chat aichat-gemini-api-main.vercel.app ](https://aichat-gemini-api-main.vercel.app/)

![](./img/219_img.png)

API 입력하고 사용해보기

![](./img/219_img_1.png)

기억을 잘하는거 같습니다.


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
