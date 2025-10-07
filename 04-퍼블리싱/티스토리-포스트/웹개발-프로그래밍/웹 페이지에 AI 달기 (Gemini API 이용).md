# 웹 페이지에 AI 달기 (Gemini API 이용)

> **원본 포스트 ID**: 216
> **발행일**: 2025-07-13 11:19:28
> **카테고리**: project/웹개발

## 📝 원문 내용

환경 설정 

**Github Desktop**

<https://desktop.github.com/download/>

[ Download GitHub Desktop Simple collaboration from your desktop desktop.github.com ](https://desktop.github.com/download/)

** Vercel **

**<https://vercel.com/>**

[ Vercel: Build and deploy the best web experiences with the AI Cloud – Vercel Vercel gives developers the frameworks, workflows, and infrastructure to build a faster, more personalized web. vercel.com ](https://vercel.com/)

**Node.js**

<https://nodejs.org/ko>

[ Node.js — Run JavaScript Everywhere Node.js® is a free, open-source, cross-platform JavaScript runtime environment that lets developers create servers, web apps, command line tools and scripts. nodejs.org ](https://nodejs.org/ko)

알아야할 함수 JS 함수

**콜백 함수**

먼저 맡은 일이 다 처리되거나 특정 상황이 발생했을 때, 비로소 호출되어 실행되는 함수이며, 

프로그램이 순서대로 기다리지 않고 다른 작업을 할 수 있게 하거나, 특정 이벤트에 반응하여 원하는 동작을 하도록 만들 때 유용하게 사용되는 것이다.

**콜백 함수 사용해보기**

// callback 쉽게말해 함수를 예약걸어놓는 것

  


//setTimeout(callback,시간)

//setTimeout(callback,3000);

  


//setInterval(callback,시간/빈도);

setInterval(myFunc,1000);

  


let count = 0;

function myFunc(){

count = count + 1;

console.log("실행 됨!" + count);

}

이 코드는 JavaScript에서 일정한 시간 간격으로 함수를 반복 실행시키는 코드입니다.

즉, setInterval 함수로 일정한 시간마다 특정 함수를 반복 실행하고 호출될 함수 이름과 시간을 적습니다,

이떄 myFunc()이 호출 될때 마다 count를 1씩 증가시키고, 실행됨! 이라는 메시지가 콘솔에 계속해서 찍히게끔 합니다.

**브라우저에서 확인해보기**

![](./img/216_img.png)

**fetch 함수**

JSON 에서 정보 탐색하기

![](./img/216_img_1.png)

제 웹사이트에 있는 영화 API 데이터입니다 이때 제목만 가지고 오고 싶으면 title이 있는 곳에 오른쪽 클릭을 눌러 경로를 복사 후에 

console.log(results[0].title);

이런식으로 찍으면 나오는 겁니다.

하지만 그전에 json 구조를 results 라는 변수에 넣어 줘야합니다.

**국가 데이터로 실습해보기**

<https://restcountries.com/v3.1/name/canada>

![](./img/216_img_2.png)

이 API는 공공API이고 CANADA에 관련한 모든것이 들어가있습니다 

이제 여기서 국가명을 적으면 수도를 알려주는 간단한 웹페이지를 만들어보겠습니다.

**js 파일**

let input = document.querySelector("input");

let button = document.querySelector("button");

let capital = document.querySelector("#capital");

  


button.addEventListener("click",function(){

let country = input.value;

// fetch(url,reqest)

fetch("<https://restcountries.com/v3.1/name/>" + country)

.then(function(response){ return response.json() })

.then(function(data){

console.log(data[0].capital[0]);

let div = document.createElement("div");

div.textContent = data[0].capital[0];

div.style.fontSize = "50px"

  


capital.innerHTML = "";

capital.append(div);

}) 

});

사용자가 버튼을 클릭하면 함수가 실행됩니다. 입력값을 가져와서 country 변수에 저장하고 fetch 함수로 API에 요청을 하고 url에 따라서 API의 정보가 바뀌니까 저런식으로 바꿉니다. 이제 HTTP 응답을 JSON 형식으로 변환 그다음 json에서 수도 정보가 있는 곳을 찾아서 설정을 합니다. 이제 브라우저에 표현이 되게끔 HTML에 표현하게 해주면 끝입니다.

**html 파일**

<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Document</title>

</head>

<body>

<div id="capital"></div>

<div>

<input type="text">

<button>요청</button>

</div>

<script src="script.js"></script>

</body>

</html>

당연히 HTML에는 삽입요청을 받는 div태그와 input button 태그는 있어야합니다.

**브라우저에서 확인하기**

![](./img/216_img_3.png)

**GET과 POST**

GET과 POST는 웹에서 데이터를 주고받는 방식, 즉 HTTP(Hypertext Transfer Protocol) 요청 메서드 중 가장 많이 사용되는 두 가지입니다. 각각의 특징과 용도는 다음과 같습니다.

GET 방식은 "정보를 요청"할 때 사용합니다.

  * 용도: 웹 서버로부터 어떤 정보를 읽거나 가져올 때 주로 사용합니다. 예를 들어, 웹 페이지를 열거나, 게시판 글 목록을 보거나, 검색 엔진에 검색어를 입력하여 결과를 얻을 때 GET 방식을 사용합니다.
  * 데이터 전달 방식: 데이터를 URL 주소 뒤에 붙여서 보냅니다. 예를 들어, www.example.com/search?query=hello와 같이 ? 뒤에 변수명=값 형태로 데이터를 붙입니다. 여러 개의 데이터는 &로 연결합니다.
  * 특징: 
    * 노출: URL에 데이터가 그대로 노출되기 때문에 보안에 취약합니다. 비밀번호나 민감한 정보를 보낼 때는 사용하지 않습니다.
    * 길이 제한: URL 길이에 제한이 있어 많은 양의 데이터를 보내기 어렵습니다.
    * 캐싱: 브라우저나 프록시 서버에서 캐싱(임시 저장)될 수 있습니다. 같은 요청을 여러 번 보내도 서버에 부담을 덜 줄 수 있습니다.
    * 북마크 가능: URL에 데이터가 포함되어 있으므로 북마크(즐겨찾기)를 할 수 있습니다.
    * 멱등성(Idempotence): 같은 요청을 여러 번 보내도 서버의 상태가 변하지 않습니다.



비유: 도서관에서 원하는 책(데이터)이 있는지 사서에게 물어보고(GET 요청) 책장 번호나 책 제목을 말해주는 것(URL에 데이터 포함)과 같습니다. 사서가 그 정보를 가지고 책을 찾아(서버가 데이터 처리) 보여주는(응답) 것이죠.

POST 방식은 "정보를 제출"할 때 사용합니다.

  * 용도: 웹 서버로 어떤 정보를 생성하거나 수정하거나 보낼 때 주로 사용합니다. 예를 들어, 회원가입 양식 작성 후 제출, 게시판에 글 작성, 파일 업로드, 로그인할 때 비밀번호를 보낼 때 POST 방식을 사용합니다.
  * 데이터 전달 방식: 데이터를 HTTP 요청의 본문(Body)에 담아서 보냅니다. URL에는 데이터가 노출되지 않습니다.
  * 특징: 
    * 보안성: 데이터가 URL에 노출되지 않으므로 GET 방식보다 보안에 유리합니다. 민감한 정보(비밀번호, 개인정보 등)를 보낼 때 적합합니다.
    * 길이 제한 없음: 전송할 수 있는 데이터 양에 사실상 제한이 없어 대용량 데이터를 보낼 수 있습니다.
    * 캐싱 불가: 캐싱되지 않습니다. 매번 요청이 서버로 직접 전달됩니다.
    * 북마크 불가능: 데이터가 본문에 있으므로 URL만으로는 요청을 재현할 수 없어 북마크할 수 없습니다.
    * 비멱등성(Non-Idempotence): 같은 요청을 여러 번 보내면 서버의 상태가 계속 변할 수 있습니다. 예를 들어, 게시글 작성 POST 요청을 두 번 보내면 같은 내용의 게시글이 두 번 생성될 수 있습니다.



비유: 우체국에서 편지나 소포(데이터)를 보내는 것(POST 요청)과 같습니다. 편지 내용(데이터)은 봉투(HTTP 본문) 안에 들어있어 겉으로 보이지 않습니다. 우체국에 보낼 내용만 전달하고, 우체국에서는 그 내용을 받아서 처리(서버가 데이터 처리)하는 것이죠.

특징 | GET | POST  
---|---|---  
주요 용도 | 정보 조회, 가져오기 | 정보 생성, 수정, 제출  
데이터 위치 | URL 주소 뒤 (?query=value) | HTTP 요청 본문 (Body)  
노출 | URL에 노출 | URL에 노출 안됨  
보안성  | 낮음 (민감 정보 부적합) | 높음 (민감 정보 적합)  
데이터 양 | 제한적 (URL 길이 제한) | 제한 없음 (대용량 가능)  
캐싱 | 가능 | 불가능  
북마크 | 가능 | 불가능  
멱등성 | 예 (반복 요청해도 서버 상태 동일) | 아니오 (반복 요청 시 서버 상태 변경 가능)  
  
** Google AI Studio 사용해보기 **

<https://aistudio.google.com/prompts/new_chat>

[ 로그인 - Google 계정 이메일 또는 휴대전화 accounts.google.com ](https://aistudio.google.com/prompts/new_chat)

**_System 프롬프트로 역할/태도/말투 부여하기 _**

![](./img/216_img_4.png)

_**API 키 생성하기 **_

![](./img/216_img_5.png)

오른쪽 위에있는 Get API Key버튼을 눌르면 API키를 볼수있습니다.

** 내 JavaScript 코드에서 fatch 로 Gemini API 연동하기 **
    
    
    https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=APIKEY
    
    
    fetch("https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-goog-api-key": "YOUR_GEMINI_API_KEY" // 여기에 실제 API 키를 넣으세요
      },
      body: JSON.stringify({
        contents: [{
          parts: [{ text: "안녕?" }]
        }]
      })
    })
    .then(function(response){ return response.json() })
    .then(function(data){
    
      console.log(data); // API 응답 결과
      
    })
    .catch(error => {
      console.error("API 호출 오류:", error); // 필수는 아님
    });

**브라우저에서 확인**

![](./img/216_img_6.png)

** 응답 데이터 구조 설명 **

data.candidates[0].content.parts[0].text 경로의 각 구조가 무엇을 의미하는지 단계별로 설명한다.

이 구조는 Gemini API로부터 받은 JSON 응답에서 모델이 생성한 최종 텍스트 결과물에 접근하기 위한 표준 경로이다.
    
    
    {
      "candidates": [ // <- candidates 배열
        {             // <- [0] 첫 번째 후보
          "content": {  // <- content 객체
            "parts": [    // <- parts 배열
              {           // <- [0] 첫 번째 파트
                "text": "여기에 최종 텍스트가 들어있습니다." // <- text 키
              }
            ],
            "role": "model"
          },
          // ... 기타 정보 (finishReason, safetyRatings 등)
        }
      ],
      // ... 기타 정보 (usageMetadata 등)
    }

**data**

  * fetch 요청 후 response.json()을 통해 받은 전체 JSON 응답 객체 그 자체이다. API가 반환한 모든 정보를 담고 있는 최상위 컨테이너이다.



**.candidates**

  * 모델이 생성한 하나 이상의 답변 후보 목록을 담고 있는 배열(Array)이다.
  * Gemini는 하나의 프롬프트에 대해 여러 개의 답변 후보를 생성할 수 있는 가능성을 열어두고 있다. candidates는 이 후보들을 배열 형태로 가지고 있다.
  * 일반적으로는 가장 품질이 좋은 하나의 답변 후보만 받게 되므로, 이 배열에는 보통 하나의 요소만 들어있다.



**.content**

  * 선택된 답변 후보(candidates[0])의 실제 내용을 담고 있는 객체이다.
  * 이 객체 안에는 누가 이 콘텐츠를 만들었는지(role, 여기서는 'model'이다)와 실제 내용물(parts)이 포함된다.



**.parts**

  * content 객체 안에 있는 콘텐츠 조각들의 목록을 담고 있는 배열(Array)이다.
  * Gemini는 텍스트, 이미지, 함수 호출 등 여러 종류의 데이터를 하나의 답변에 섞어서 보낼 수 있다 (멀티모달). parts는 이러한 다양한 형태의 데이터 조각들을 담는 배열이다.
  * 단순한 텍스트 응답의 경우, 이 배열에는 텍스트를 담은 하나의 요소만 존재한다.



**.text**

  * 첫 번째 파트(parts[0]) 안에 있는 **최종 텍스트 데이터** 이다.
  * string 타입이며, 모델이 생성한 실제 문장, 즉 사용자에게 보여줄 최종 결과물이다.



**요약하자면, 이 경로는 다음과 같은 흐름으로 원하는 데이터에 접근하는 과정이다.**

> "전체 응답(data)에서 → 답변 후보 목록(candidates)을 꺼내 → 그중 첫 번째 후보([0])를 선택한 뒤 → 그 후보의 내용물(content)을 열어 → 여러 조각 중 첫 번째 조각(parts[0])을 골라 → 그 안에 담긴 최종 텍스트(.text)를 읽는다."  
> 

**배열 메소드 **

배열 메소드 (Array Methods)

<https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array>

[ Array - JavaScript | MDN 다른 프로그래밍 언어의 배열과 마찬가지로, Array 객체는 여러 항목의 컬렉션을 단일 변수 이름 아래 저장할 수 있고, 일반적인 배열 연산을 수행하기 위한 멤버가 있습니다. developer.mozilla.org ](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array)
    
    
    let arr = ["일","이","삼"];
    
    arr.push("사");    // 배열 맨뒤에 값 추가
    arr.pop();        // 배열 마지막 값 삭제
    
    arr.unshift("영"); // 배열 맨앞에 값 추가
    arr.shift();      // 배열 첫번째에 값 삭제
    
    arr.splice();     // 배열 특정 위치에 요소를 추가하거나 삭제
    arr.splice(1,2); 	// 1번(두번째) 인덱스부터 2개를 삭제

**forEach**
    
    
    let arr = ["빨강","초록","파랑"];
    
    // forEach는 배열에 들어있는 각 요소(item)를 처음부터 끝까지 하나씩 매개변수로 꺼내서, 
    // 우리가 전달한 함수(function)를 실행해준다. 
    // 이때 함수는 각 요소의 값과 해당 요소가 배열의 몇 번째에 있는지(index)를 알 수 있다.
    arr.forEach( function(item, index){ 
      console.log(item,index);
    });

forEach 로 여러개 요소
    
    
    let arr = ["빨강","초록","파랑"];
    let body = document.querySelector("body");
    
    arr.forEach( function(item, index){ 
    
    	let p = document.createElement("p");  // p 요소
    	p.textContent = item;                 // 요소에 배열의 각 텍스트 입력
    	
    	body.append(p);                       // body 에 p 요소 추가
    	
    });

**다른 배열 메소드들 **

**filter**
    
    
    // filter는 배열의 각 요소(item)를 우리가 전달한 함수로 테스트하여,
    // 그 함수의 반환 값이 'true'인 요소들만 모아 '새로운 배열'로 만들어 돌려준다.
    // 함수는 각 요소의 값(item)과 인덱스(index)를 사용할 수 있다.
    let ages = [10, 25, 18, 30];
    let adults = ages.filter( function(item, index){
      return item >= 19; // 나이가 19 이상이면 true, 이 요소는 새 배열에 포함된다.
    });
    console.log(adults); // [25, 30]

**find**
    
    
    // find는 배열에서 우리가 전달한 함수를 만족하는 '첫 번째 요소 하나만' 찾아 돌려준다.
    // 만약 만족하는 요소가 없으면 undefined를 반환한다.
    // 함수는 각 요소의 값(item)과 인덱스(index)를 사용할 수 있다.
    let names = ["철수", "영희", "바둑이"];
    let foundName = names.find( function(item, index){
      return item === "영희"; // 이름이 "영희"인 첫 번째 요소를 찾는다.
    });
    console.log(foundName); // "영희"

**sort**
    
    
    // sort는 배열의 요소들을 정렬하며, '원본 배열 자체를 변경'시킨다.
    // 비교 함수를 전달하지 않으면 요소들을 문자열로 변환해 유니코드 순서로 정렬한다.
    // 숫자를 제대로 정렬하거나 특정 기준으로 정렬하려면 '비교 함수'를 전달해야 한다.
    let mixedNumbers = [10, 5, 100, 1];
    mixedNumbers.sort( function(a, b){ // 비교 함수는 두 요소 a와 b를 받는다.
      return a - b; // a - b가 음수면 a가 앞으로, 양수면 b가 앞으로, 0이면 그대로 (오름차순).
    });
    console.log(mixedNumbers); // [1, 5, 10, 100]

여기까지가 웹 페이제에 AI달기전 준비운동이다 다음 포스트에서 실제로 구현하고 배포까지 마쳐보겠습니다.


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
