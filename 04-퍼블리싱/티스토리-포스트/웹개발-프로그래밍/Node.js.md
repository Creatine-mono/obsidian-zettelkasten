# Node.js

> **원본 포스트 ID**: 180
> **발행일**: 2025-06-14 00:09:48
> **카테고리**: project/웹개발

## 📝 원문 내용

**Node.js**

* * *

Node.js는 javascript 코드를 브라우저 밖에서 실행할 수 있게 해주는 런타임 환경이다.

런타임(Runtime) == 프로그램이 구동되는 환경

다시 말해 Node.js 는 크롬브라우저와 같이 자바스크립트가 실행되는 환경입니다.

**Node.js 구조**

* * *

![](./img/180_img.png)

**서버 구조**

* * *

![](./img/180_img_1.png)

  1. **Model 데이터베이스**
  2. **Router== Controller 주소(URL)**
  3. **View HTML(화면)**



이 모든 것들을 만들 수 있게 도와주는 게 Node.js입니다.

그리고 더 쉽게 서버 구조 를 만들 수 있게 도와주는 Express.js라는 도구를 이용해서 이용할 껍니다.

그리고 app.js로 서버를 킵니다.

**Node.js 설치**

* * *

<https://nodejs.org/ko>

[ Node.js — 어디서든 JavaScript를 실행하세요 Node.js® is a JavaScript runtime built on Chrome's V8 JavaScript engine. nodejs.org ](https://nodejs.org/ko)

![](./img/180_img_2.png)

설치가 제대로 됐는지 확인

![](./img/180_img_3.png)

** Node.JS 프로젝트 폴더 생성과 서버 구조 살펴보기**

* * *

git-Bash 에서 바탕화면으로 이동

![](./img/180_img_4.png)

파일 생성

![](./img/180_img_5.png)

Node.js 프로젝트 폴더 생성 과 구조 살펴보기 

![](./img/180_img_6.png) node 프로젝트임을 명시 ![](./img/180_img_7.png)

서버 구조에 필요한 폴더, 파일 생성(router, views, model,app.js)

![](./img/180_img_8.png) ![](./img/180_img_9.png)

생성된 파일 확인

![](./img/180_img_10.png)

vscode로 확인

![](./img/180_img_11.png)

파일 생성

![](./img/180_img_12.png)

Express와 서버 실행

* * *

express 설치

![](./img/180_img_13.png)

이제 vs code로 들어가보면 node_modules라는 폴더가 생긴걸 볼수 있다.

![](./img/180_img_14.png)

그리고 또 package.json파일 들어가보면 expree가 설치되어있다고 쓰여있다.

app.js 수정

express 를 사용할 수 있는 코드 삽입

const express = require('express');

const app = express();

app.get("/", function(req,res)

{res.send('Hello World');

})

주소를 만드는 app.get을 실행시키고 안에 함수를 넣습니다. 함수 내용은 요청 과 응답입니다 주소를 치고 들어가면 Hello World를 응답하는 코드입니다.

app.listen(3000,function(req,res){

console.log("서버가 실행되고 있다!")

})

여기서는 컴퓨터의 스위치를 만드는 과정입니다. 3000번 포트를 이용한다.

터미널에서 확인해보기

![](./img/180_img_15.png)

이런식으로 서버가 돌아가고 있음을 확인할 수 있다.

크롬에서 확인해보기

![](./img/180_img_16.png)

주소 하나 더 만들기

서버가 실행되고있는 중 이므로 서버를 끄고 만들어보겠습니다

app.get("/about", function(req,res)

{res.send('About page');

})

![](./img/180_img_17.png)

이런식으로 한페이지 씩 만들때마다 서버를 껐다 키긴 너무 귀찮으니까 자동으로 해주는 도구를 설치 합니다.

![](./img/180_img_18.png)
    
    
     supervisor app.js

위 명령어로 실행시켜줄 수 있습니다. 이제 변경이 있을때마다 서버를 알아서 껏다가 켜줍니다.

보안관련 도구인 helmet 알아보기

<https://www.npmjs.com/package/helmet>

[ helmet help secure Express/Connect apps with various HTTP headers. Latest version: 8.1.0, last published: 3 months ago. Start using helmet in your project by running `npm i helmet`. There are 5801 other projects in the npm registry using helmet. www.npmjs.com ](https://www.npmjs.com/package/helmet)

npm helmet 설치하기

![](./img/180_img_19.png)

코드에 helmet 적용

const express = require('express');

const helmet = require('helmet');

const app = express();

  


app.use(helmet());

**npm rank 알아보기**

<https://gist.github.com/anvaka/8e8fa57c7ee1350e3491>

[ npm rank npm rank. GitHub Gist: instantly share code, notes, and snippets. gist.github.com ](https://gist.github.com/anvaka/8e8fa57c7ee1350e3491)

개발자들의 npm 도구 순위입니다.

주소가 많아지면 app.js의 페이지가 너무 커지기때문에 프로트엔드 공부할때 css 분리한것 처럼

주소 부분을 라우터 파일로 옮깁니다.

const express = require('express');

const router = express.Router();

  


router.get("/", function(req,res)

{res.send('Hello World');

})

  


router.get("/about", function(req,res)

{res.send('About page');

})

module.exports = router

밖으로 내보낸다음 app.js에서 받읍시다

const mainRouter = require('./router/mainRouter')

app.use('/',mainRouter)

크롬에서 확인하기

![](./img/180_img_20.png)

그리고 저 app.use 코드 뒤에있는 /이걸 수정해봅시다.

app.use('/pk42ac',mainRouter)

![](./img/180_img_21.png) ![](./img/180_img_22.png)

저 부분은 디폴트 값입니다. 라우터가 많이지면 관리하기 편하라고 이러한 디폴트값을 넣어놓곤 합니다.

**API 만들어보기, GET과 POST 방식**

* * *

무료 API 구경해보기

![](./img/180_img_23.png)

Key:Value으로 이루어진거 같네요 제가 만든 서버에도 한번 key:value값을 내보내보겠습니다.

router.get("/", function(req,res)

{res.send({"Key":"Value"});

})

![](./img/180_img_24.png)

조촐하지만 비슷하네요

코드를 깔끔하게 볼 수 있는 JSON Viewer 설치

![](./img/180_img_25.png) ![](./img/180_img_26.png)

GET 방식 알아보기

GET방식은 알다시피 가는 정보나 원하는 형태의 정보를 URL에 표시해준다

router.get("/", function(req,res){

let QUERY = req.query;

console.log("[QUERY]")

![](./img/180_img_27.png) ![](./img/180_img_28.png)

이런식으로 URL에 page3을 요청하게된다면 터미널에 다시 찍히는 걸 볼 수 있다.

이렇게 오는 요청에 데이터를 담아서 보내면 그게 API입니다.

POST 방식

router.post("/postapi", function(req,res)

{res.send('POST API');

})

post방식은 get과 다르게 URL 에서 확인할 수 없으니 postman을 이용하겠습니다.

<https://www.postman.com/>

[ Postman: The World's Leading API Platform | Sign Up for Free Accelerate API development with Postman's all-in-one platform. Streamline collaboration and simplify the API lifecycle for faster, better results. Learn more. www.postman.com ](https://www.postman.com/)

![](./img/180_img_29.png)

get방식과 다르게 여기서도 URL에 데이터를 넣을순 없고 body에 넣어서 보내야한다

body 로 보내봅시다

코드 수정

router.post("/postapi", function(req,res){

let body = req.body;

console.log(body)

res.send('POST API');

})

body 에 보내고 터미널에서 확인

![](./img/180_img_30.png) ![](./img/180_img_31.png)

안보이네요

app.js에서 body에서 보낸걸 확인할수있는 코드를 추가 하겠습니다.

app.use(express.json());

app.use(express.urlencoded());

다시 보내기

![](./img/180_img_32.png) ![](./img/180_img_33.png)

잘 나옵니다.

**HTML, CSS 그림 파일 보여주기 (with 템플릿엔진 EJS)**

* * *

먼저 HTML, CSS를 보여주기위해서 app.js에서 연결해주겠습니다.

ejs 설치

![](./img/180_img_34.png)

const ejs = require('ejs');

app.js 에서 ejs 실행하는 코드 삽입

app.set('view engine', 'ejs');

app.set('views', './views')

app.use('/public',express.static(__dirname + '/public'));

그림파일과 HTML 파일을 전달해줄수있는 코드 삽입

라우터 파일에 index.html 파일을 열어주는 코드 삽입합니다

router.get("/", function(req,res){

res.render('index')

})

index.html 만들기

<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Document</title>

</head>

<body>

<h1>안녕하세요</h1>

</body>

</html>

이렇게 하면 

![](./img/180_img_35.png)

오류가 납니다..

오류가 나는 이유는 확장자 이름이 html이기 때문입니다. ejs는 확장자 명도 ejs로 바꿔줘야합니다 

![](./img/180_img_36.png)

데이터를 한번 보내봅시다 view engine 사용법

router.get("/", function(req,res){

res.render('index',{title:"EJS 메인페이지"})

})

이런식으로 데이터와 같이 보내주고 

<body>

<h1><%= title %></h1>

</body>

html body부분에 저걸 삽입하면

![](./img/180_img_37.png)

css 보여주기

![](./img/180_img_38.png)

css파일 하나 만들어줍니다

<link rel="stylesheet" href="/public/main.css">

html파일 에 링크 걸어주고

* {

color: red;

}

css 파일 수정 하고 결과 확인

![](./img/180_img_39.png)


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
