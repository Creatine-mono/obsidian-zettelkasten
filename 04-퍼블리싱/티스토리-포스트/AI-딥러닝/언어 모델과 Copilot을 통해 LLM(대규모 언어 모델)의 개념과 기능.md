# 언어 모델과 Copilot을 통해 LLM(대규모 언어 모델)의 개념과 기능

> **원본 포스트 ID**: 223
> **발행일**: 2025-07-16 23:34:48
> **카테고리**: project/AI 개발

## 📝 원문 내용

![](./img/223_img.png)

위 사진에 따르면 1등부터10등까지 모두다 IT관련 기업이다.

<https://news.mt.co.kr/mtview.php?no=2022090610275766691>

[ 1500% 폭등하다 70% 폭락..메타버스 고꾸라진 이유는 - 머니투데이 [메타버스株 폭락, 신기술? 신기루?]②지난해 주식시장에서 가장 핫한 테마는 "메타버스"였다. 메타버스가 차세대 산업으로 주목받으면서 메타버스 관련 주가도 고공행진했다. 하지만 올 들어 news.mt.co.kr ](https://news.mt.co.kr/mtview.php?no=2022090610275766691)

<https://about.fb.com/ko/news/2024/07/introducing-llama-3-1-our-most-capable-models-to-date/>

[ 메타의 현존 가장 강력한 AI 모델, Llama 3.1을 소개합니다 | Meta 소개 *영어 원문 보기 주요 내용 Meta는 오픈 소스 AI를 위해 최선을 다하고 있습니다. 오픈 소스가 개발자, Meta, 그리고 우리 모두에게 왜 좋은지를 설명하는 Mark Zuckerberg의 서한을 확인해 보세요. 모두 about.fb.com ](https://about.fb.com/ko/news/2024/07/introducing-llama-3-1-our-most-capable-models-to-date/)

![](./img/223_img_1.png)

<https://youtu.be/3z2ln2FEOTE?si=nZzjgm5kEs1jdfV6>

**Generative AI market layout**

  1. Contents & Services
  2. Platform (Microsoft, Google, Facebook...)
  3. AI (OpenAI GPT, Google Gemini...)
  4. Cloud(Azure, AWS, GCP...)
  5. Network (SKT, KT, AT&T Mobile, NTT...)
  6. Device (Apple, Samsung ...)



<https://www.joongang.co.kr/article/25228165>

[ 샘 올트먼 9000조 투자 유치, 젠슨 황 맞춤형 설계…AI·GPU 대표주자 맞붙다 | 중앙일보 샘 올트먼 오픈AI 최고경영자(CEO)와 젠슨 황 엔비디아 CEO-. 또 다른 강자 엔비디아는 이런 올트먼의 계획에 응수라도 하듯 맞춤형 AI반도체 시장 공략에 나섰다. 같은 날 로이터에 따르면 엔비디 www.joongang.co.kr ](https://www.joongang.co.kr/article/25228165)

**ChatGPT**

![](./img/223_img_2.png)

| 무료 | 유료  
---|---|---  
학습한 데이터 | ChatGPT 3.5  
ChatGPT 4  
ChatGPT 4o mini | ChatGPT 4o  
특징 | 빠른 결과물 생성  
텍스트 위주의 결과물 | 텍스트, 음성, 이미지, 동영상 처리  
Browser with Bing  
Advanced Data Analysis  
Max Data | ChatGPT 3.5 4096 tokens  
ChatGPT 4o mini 128,000 tokens | 128,000 tokens  
비용 / 제한 | 무료 | 유료  
  
![](./img/223_img.jpg)

<https://www.newsmc.net/news/articleView.html?idxno=67323>

[ 이러다 미국 제칠라... 중국, 이번엔 1조 파라미터 모델 공개 - 뉴스메카 [뉴스메카=박형배 기자] 중국의 혁신적 AI 스타트업 Moonshot AI가 세계 최초로 1조(1 trillion) 파라미터를 탑재한 초대형 오픈소스 언어모델 \'Kimi K2\'를 전격 공개했다. 이로써 Moonshot AI는 글로벌 AI 패 www.newsmc.net ](https://www.newsmc.net/news/articleView.html?idxno=67323)

![](./img/223_img_3.png)

<https://openai.com/ko-KR/index/dall-e-3/>

![](./img/223_download.png)

**이미지 생성 AI인 dall-e-3**

<https://openai.com/ko-KR/sora/>

![](./img/223_download_1.png)

**동영상 생성 AI인 Sora**

**Transformer**

**GPT(generative pre-trained transformer)**

![](./img/223_img_4.png) https://gaussian37.github.io/dl-concept-transformer/

** GPT는 어떤식으로 학습할까?  
**

**GPT3.5기준**

데이터세트 | 토큰 | 교육 비율  
---|---|---  
일반 크롤링 | 4100억개 | 60%  
웹텍스트 | 190억개 | 22%  
책1 | 120억개 | 8%  
책2 | 550억개 | 8%  
위키백과 | 30억개 | 3%  
  
**토큰이란?**

토큰은 컴퓨터나 네트워크 시스템, 특히 인증(Authentication), 권한 부여(Authorization), 또는 데이터 처리 과정에서 사용하는 단위 정보 조각입니다. 사용하는 맥락에 따라 의미가 달라지며, 크게 아래와 같은 용도로 나뉩니다.

* * *

**1\. 인증·보안에서의 토큰**

웹 서비스나 API에서 자주 등장하며, 사용자의 인증 상태나 권한 정보를 담고 있는 문자열입니다.  
예: 로그인 후 서버가 클라이언트에 발급하는 JWT(Json Web Token).

  * 기능: 인증 확인, 권한 검증
  * 예시: 
    * eyJhbGciOiJIUzI1NiIsInR... (JWT 문자열)
  * 사용 예: 
    * 사용자가 로그인하면 서버는 토큰을 발급 → 클라이언트가 요청할 때 이 토큰을 포함시킴 → 서버는 토큰을 확인해 사용자 인증을 처리



* * *

**2\. NLP(자연어처리)에서의 토큰**

텍스트 데이터를 처리할 때, 문장을 작은 단위로 쪼갠 결과물입니다.  
주로 단어, 형태소, 문자, 혹은 subword 단위로 나눕니다.

  * 기능: 텍스트 분석, 모델 입력 전 전처리
  * 예시: 
    * 문장: "나는 사과를 먹었다."
    * 토큰화 결과 (단어 기준): ["나", "는", "사과", "를", "먹", "었", "다", "."]
    * GPT에서는 subword 단위로 나눔 (예: e, ating, ##ly 같은 형태)



* * *

**3\. 블록체인에서의 토큰**

코인과는 다르게 특정 플랫폼(예: 이더리움) 위에서 만들어진 디지털 자산입니다.

  * 기능: 거래 수단, 유틸리티 제공, 거버넌스 투표 등
  * 예시: 
    * ERC-20 토큰 (USDT, UNI 등)
    * NFT (ERC-721)



웹사이트에서 확인해보기

**영어**

![](./img/223_img_5.png)

**한국어**

![](./img/223_img_6.png)

각각의 AI들이 언어를 학습하는 방법

**BERT vs GPT**

BERT: 양방향 마스킹 언어 모델 (Bidirectional Encoder Representations from Transformers)

▶ 학습 방식 (MLM: Masked Language Modeling)

  * 문장에서 임의의 단어를 [MASK]로 가린 후, 해당 단어가 무엇인지 예측
  * 모델은 문장의 앞뒤 모든 문맥을 동시에 고려함 → 양방향 학습



예시:

입력: "나는 오늘 [MASK]에 갔다."

예측: [MASK] → "학교", "병원" 등 

장점:

  * 문맥 이해에 강함 (특히 문장 의미 파악, 분류, 유사도 분석에 유리)
  * 양방향성 때문에 단어가 등장하는 전체 상황을 파악 가능



* * *

GPT: 자동회귀 언어 모델 (Generative Pretrained Transformer)

▶ 학습 방식 (AR: Autoregressive Language Modeling)

  * 문장을 왼쪽부터 순차적으로 입력, 다음 단어를 예측하는 방식
  * 예측 시 현재까지 본 단어만 사용 (한 방향, 오른쪽으로 진행)



예시:

입력: "나는 오늘"

예측: 다음 단어 → "학교에", 다음 → "갔다", ... 

장점:

  * 자연스러운 문장 생성 능력 우수
  * 대화, 글쓰기, 코드 생성 등에 매우 강력



**Education Industry**

**Duolingo**

**시스템 구조**

    * Large Language Model (GPT‑4 등)
      * 텍스트 생성, 해설, 대화 역할 수행
    * 프롬프트 설계 
      * “System” → 대화 톤, 난이도, 맥락 설정
      * “Assistant” → 실제 AI 캐릭터
      * “User” → 학습자 입력에 따라 반응
    * 콘텐츠 생성 + 리뷰
      * AI가 만든 문제나 대답은 전문가가 검수 후 앱에 반영
    * 맞춤 피드백 루프
      * 실시간 사용자 데이터 분석 후 난이도·콘텐츠 개인화



**하는 역할**

  * 문법 오류 해설 (Explain My Answer)
  * 역할놀이(Roleplay) 기능 통한 실전 대화 연습
  * 가상 AI 캐릭터와의 회화 훈련
  * 학습 수준에 맞춘 콘텐츠 제공
  * 


**Coursera**

**시스템 구조**

  * 강의 플랫폼 + AI 학습 엔진 
    * 일반 콘텐츠와 AI 기반 인터랙션 기능 통합
  * Large Language Model 기반 AI 튜터 
    * 질문 답변, 해설, 실시간 피드백 수행
  * 개인화 추천 알고리즘 
    * 수강 이력, 관심사, 학습 성과 기반 강의 추천
  * 자동 평가 및 추적 시스템 
    * 퀴즈 채점, 과제 피드백, 학습 진행률 관리



**하는 역할**

  * 사용자 수준에 맞는 강의 자동 추천
  * 퀴즈·과제에 대한 AI 자동 피드백 제공
  * 실시간 질문 응답 (AI 튜터 기능)
  * 대규모 온라인 수업의 학습 효율 향상
  * Generative AI, AI for Everyone 등 AI 주제 교육 제공



**Speak**

**시스템 구조**

  * 음성 인식 엔진 → 발음 분석
  * GPT 기반 대화 모델 → 실시간 응답
  * 피드백 엔진 → 문법/발음 점수화 및 피드백



**하는 역할**

  * 사용자의 발음·문법 실시간 교정
  * AI와 실제 대화하며 회화 훈련
  * 대화 상황 맞춤 시나리오 제공 (공항, 레스토랑 등)
  * 반복 학습 및 진행 추적 기능



**Qanda**

**시스템 구조**

  * OCR 인식 → 수학 문제 추출
  * MathGPT (전문 LLM)로 자동 풀이 생성
  * AI + 실제 튜터 병행
  * 커뮤니티 기반 학습 도우미 기능 포함



**하는 역할**

  * 수학/과학 문제 자동 인식 및 풀이
  * 단계별 설명 제공
  * 실시간 질문 응답 (튜터 또는 AI)
  * 학습 관리 기능 (타이머, 커뮤니티 등)



**Team Sparta**

**시스템 구조**

  * ChatGPT API 기반 코드 분석기
  * AI 코드 채점 모듈
  * AITC 인증시험 시스템 (5단계 AI 역량 평가)
  * 해커톤 플랫폼 연계



**하는 역할**

  * 실시간 코드 피드백 및 채점
  * AI 활용 능력 인증 시험(AITC) 제공
  * 기업·학습자 대상 실전 AI 도입 교육
  * 커뮤니티 기반 실습형 학습 제공



**그외에**

**HeyGen 번역 AI**

**<https://youtu.be/YbrG7MONoGc?si=qzcfFhiMlyrtMuFZ>**

**Recraft**AI 이미지 생성****

<https://www.recraft.ai/>

[ Image Generation for Designers - Recraft Premium image generation and editing tool. Store and share your own styles, create, fine-tune, upscale, and perfect your visuals. www.recraft.ai ](https://www.recraft.ai/)

**ElevenLabs 목소리 변조 AI**

<https://elevenlabs.io/>

[ Free Text to Speech & AI Voice Generator | ElevenLabs Create the most realistic speech with our AI audio tools in 1000s of voices and 70+ languages. Easy to use API's and SDK's. Scalable, secure, and customizable voice solutions tailored for enterprise needs. Pioneering research in Text to Speech and AI Voice elevenlabs.io ](https://elevenlabs.io/)

**Gamma ai**

**<https://gamma.app/>**

[ AI로 빠르게 프레젠테이션, 웹사이트 등을 제작하세요 | Gamma Gamma는 프레젠테이션, 웹사이트 등을 손쉽게 만들 수 있는 무료 AI 디자인 파트너입니다. 코딩이나 디자인 기술이 필요하지 않습니다. gamma.app ](https://gamma.app/)


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

**태그**: #projectAI개발
**상태**: 🌱 씨앗 (제텔카스텐 통합 대기)
**변환일**: 2025-10-07
