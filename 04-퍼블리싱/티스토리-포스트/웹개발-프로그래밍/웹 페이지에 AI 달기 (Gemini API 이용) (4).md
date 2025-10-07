# 웹 페이지에 AI 달기 (Gemini API 이용) (4)

> **원본 포스트 ID**: 221
> **발행일**: 2025-07-15 15:55:24
> **카테고리**: project/웹개발

## 📝 원문 내용

#### **랜덤 Random**

Math.random()
    
    
    Math.random() // 0 ~ 1 사이의 랜덤한 값

랜덤한 소수값 생성
    
    
    Math.random() * 5 // 0 ~ 5 사이의 랜덤한 수소값

랜덤한 정수값 생성
    
    
    Math.floor(Math.random() * 5) // 0 ~ 4 중 랜덤한 정수 값
    Math.floor(Math.random() * 100) // 0 ~ 99 중 랜덤한 정수 값

**타로 카드 AI봇**

조금 더 복잡한 기능을 다루는 AI봇 구현

카드 랜덤 선택 함수
    
    
    // 선택할 3개 카드를 담을 배열
    let selectedCards = [];
    
    // 카드 랜덤 선택 함수
    function selectRandomCard(){
    	// 인덱스 랜덤 선택
    	let randomIndex = Math.floor(Math.random() * tarotCards.length);
    	
    	// 해당 인덱스 데이터 뽑아내기
    	let selected = tarotCards.splice(randomIndex, 1)[0];
    	
    	// 카드 뒤집힘 랜덤으로 정하기
    	selected.reverse = Math.random() < 0.5;
    	
    	// 선택 배열에 해당 카드데이터 추가
    	selectedCards.push(selected);
    }

카드 3장 선택 및 웹페이지에 표현
    
    
    // 현재 상태 저장
    let status = "waiting";
    
    function drawCards(){
      selectedCards = [];
      selectRandomCard();
      selectRandomCard(); 
      selectRandomCard();
    
      selectedCards.forEach(card => {
        let cardElement = document.createElement("div");
        cardElement.className = "card";
        if(card.reverse){
          cardElement.classList.add("reverse");
        }
      
        let cardImage = document.createElement("img");
        cardImage.src = `cards/${card.filename}`;
        cardImage.alt = card.name;
        cardElement.append(cardImage);
      
        selectedCardContainer.append(cardElement);
      });
    
    	// 카드 세팅후 상태변경
      status = "cards_drawn";
    
    }

**최종 웹사이트**

<https://ai-tarot-vercel-main-2.vercel.app/>

[ AI Tarot ai-tarot-vercel-main-2.vercel.app ](https://ai-tarot-vercel-main-2.vercel.app/)


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
