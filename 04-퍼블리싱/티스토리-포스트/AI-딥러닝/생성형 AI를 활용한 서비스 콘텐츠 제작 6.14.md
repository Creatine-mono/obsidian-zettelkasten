# 생성형 AI를 활용한 서비스 콘텐츠 제작 6.14

> **원본 포스트 ID**: 176
> **발행일**: 2025-06-13 18:25:12
> **카테고리**: 대외활동/생성형 AI를 활용한 서비스 콘텐츠 제작

## 📝 원문 내용

![](./img/176_img.png)

****

**인공지능 (Artificial Intelligence)**

* * *

**정의**

  * 컴퓨터가 인간의 지능적인 행동을 모방하여 학습, 추론, 문제 해결, 언어 이해 등을 수행할 수 있도록 하는 기술 (MaCarthy, 1956)
  * 지능(Intelligence): 인간이 행하는 지적 작업의 주체



**종류**

  * 예측 모델 (Predictive Models): Regression Models, Decision Trees, Random Forests
  * 생성 모델 (Generative Models): GAN, GPT, DALL-E
  * 강화 학습 (Reinforcement Learning): Deep Q-Network



**머신 러닝 (Machine Learning)**

* * *

**정의**

  * 머신이 코드로 명시되지 않은 동작을 데이터로부터 학습하여 실행할 수 있도록 하는 알고리즘
  * 데이터로부터 일관된 패턴 또는 새로운 지식을 찾아내(학습하)는 방법
  * 학습 이후 새로운 데이터에 대하여 학습된 내용으로 처리하는 것



**학습 (Learning)**

  * 학습이란 "어떤 작업에 대해 특정 기준으로 측정한 성능이 새로운 경험으로 인해 개선되었다 면, 그 프로그램은 어떤 작업에 대해 특정 기준의 관점에서 새로운 경험으로 부터 ‘배웠다‘라 고 말할 수 있다." (Tom M. Mitchell, 1998)



**딥러닝 (Deep Learning)**

* * *

**정의**

  * Perceptron: 인공신경망의 한 종류 (Frank Rosenblatt, 1957)
  * Multi Layer Perceptron: 여러 층의 퍼셉트론을 쌓아서 동작(Input - Hidden - Output)
  * Deep Neural Network: Hidden Layer가 2개 이상인 구조



**신경망 실습**

[https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=4,2&seed=0.31832&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false](https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=4,2&seed=0.31832&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false)

[ Tensorflow — Neural Network Playground Tinker with a real neural network right here in your browser. playground.tensorflow.org ](https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=4,2&seed=0.31832&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false)

**구글 코랩으로 실습**

코랩을 하기 전에 키를 받아야한다고 한다 키는 ngrok에서 무료로 받을 수 있다.

<https://ngrok.com/>

[ ngrok | API Gateway, Kubernetes Ingress, Webhook Gateway ngrok simplifies app delivery by unifying API gateway, Kubernetes ingress, multi-cluster load balancing and more with ngrok's Universal Gateway. ngrok.com ](https://ngrok.com/)

nogrok 은 무엇일까?

ngrok은 로컬에서 실행 중인 애플리케이션(예: 웹 서버)을 외부 인터넷에서 접근할 수 있도록 도와주는 보안 터널링 서비스입니다. 쉽게 말하면, 당신의 컴퓨터에서 돌아가는 웹사이트를 외부에서 볼 수 있도록 URL을 만들어주는 도구입니다.

**강아지 고양이 분류 AI**

![](./img/176_92969_25283_5321.jpg)

![](./img/176_img.jpg)

위 사진 두개를 AI로 예측해보겠습니다.

![](./img/176_img_1.png) ![](./img/176_img_2.png)

동영상도 분류가 가능합니다.

동영상은 처음에 고양이를 초점을 맞췄다가 나중에 강아지로 바뀌는 영상입니다 프레임별로 구분하는 AI 모습입니다.

![](./img/176_img_3.png) ![](./img/176_img_4.png)

**Object Detection**

* * *

**정의**

  * 이미지나 비디오에서 객체의 위치를 찾고 해당 객체의 종류를 분류하는 컴퓨터 비전 기술
  * 객체의 경계 상자(Bounding Box)를 예측하여 객체를 감지하고, 이미지나 영상 내에서 여러 객체를 동시에 식별



![](./img/176_img_1.jpg) https://deepbaksuvision.github.io/Modu_ObjectDetection/posts/01_00_What_is_Object_Detection.html

AI는 분류, 예측하는 AI만 있는게 아니고 탐지형 AI 도 있다.

**구글 코랩으로 실습하기**

실습한 AI는 마스크를 썻는지 안썻는지 탐지해주는 AI다.

![](./img/176_img_2.jpg)

위 사진을 AI로 탐지 해보겠습니다.

![](./img/176_img_5.png)

코가 보이게 마스크를 썼으면 마스크를 안썼다고 한다.

**생성 모델 (Generative Models)**

* * *

**정의**

  * 주어진 데이터 분포를 학습하여 새로운 데이터를 생성할 수 있는 모델
  * 텍스트, 이미지, 음성 등 다양한 데이터를 생성하는 데 활용되며, 데이터의 확률 분포를 기반 으로 새로운 샘플을 생성



**종류**

  * VAE (Variational Autoencoder): 데이터의 잠재 변수를 확률적으로 모델링
  * GAN (Generative Adversarial Networks): 두 신경망(생성자와 판별자)이 경쟁하는 구조
  * Transformer (BERT, GPT): 텍스트 생성을 위한 모델



오늘 수업에서는 생성 모델 중에 LLM을 집중적으로 실습하고 공부했다

이번 실습은 OPENAI 의 KEY 를 받아서 실습했다.

**OPENAI KEY 받는법**

* * *

**1 단계: OpenAI 계정 생성 또는 로그인**

**1. 브라우저에서 <https://platform.openai.com> 접속**

![](./img/176_img_6.png)

**2. 우측 상단의 Sign up  버튼 클릭 (계정이 없다면 생성)**

**2 단계: API 사용 목적 설정 (최초 가입 시)**

**- 개인/기업/연구/교육 목적 등 선택지 중 하나를 선택**

![](./img/176_img_7.png)

>>> Organization name >>> Personal (입력)

>>> What best describes you? >>> Somewhat technical (선택)

**> >> Create organization  (클릭)**

![](./img/176_img_8.png)

**> >> I'll invite my team later (클릭)**

![](./img/176_img_9.png)

>>> My test key >>> Copy  (클릭하여 복사 후 안전하게 저장) 

**> >> Continue  (클릭) **

![](./img/176_img_10.png)

** I'll buy credits later (클릭)**

API 키 값을 받았으면 코랩에 등록을 하면 된다.

![](./img/176_img_11.png)

**코랩으로 실습하기**

* * *

수업하기 전 코드를 보여주면서 어떤식으로 작동하는 지 설명해주셨다.
    
    
    # 모델 설정
    model = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-4o-mini")
    
    # 마케팅 문구 생성 프롬프트
    slogan_prompt_template = """
    당신은 마케팅 전문가입니다.
    입력된 키워드에 기반하여 해당 제품 또는 서비스에 사용할 수 있는 마케팅 문구를 3가지 제안하세요.
    각 문구는 간결하고 눈길을 끌며, 30자 이내로 작성해주세요.
    
    키워드: {keyword}
    """
    
    slogan_prompt = PromptTemplate.from_template(slogan_prompt_template)
    slogan_chain = LLMChain(llm=model, prompt=slogan_prompt)
    
    # 마케팅 계획서 프롬프트
    plan_prompt_template = """
    당신은 마케팅 전략가입니다.
    아래 마케팅 문구를 중심으로, 해당 제품의 간단한 마케팅 계획서를 작성하세요.
    계획서는 다음 내용을 포함해야 합니다:
    1. 문구의 핵심 메시지
    2. 타겟 고객
    3. 활용 채널 및 매체
    4. 기대 효과
    
    마케팅 문구: "{slogan}"
    """

![](./img/176_img_12.png)

하면 이런식으로 나온다 GTP 의 무료 버전을 사용하고 있는 중이라 엄청나게 자세하거나 그러진않지만 이런식으로 마케팅만을 위한 AI 서비스를 배포해서 사업을 할 수 있다는 걸 보여주시는 것 같았습니다.

이번에 수정해서 다시한번 물어보겠습니다.
    
    
    # 마케팅 계획서 프롬프트
    plan_prompt_template = """
    당신은 마케팅 전략가입니다.
    아래 마케팅 문구를 중심으로, 해당 제품의 간단한 마케팅 계획서를 작성하세요.
    계획서는 다음 내용을 포함해야 합니다:
    1. 문구의 핵심 메시지
    2. 타겟 고객
    3. 활용 채널 및 매체
    4. 기대 효과
    5. 마지막 문구

그냥 저런식으로 마지막 문구만 추가했습니다.

![](./img/176_img_13.png)

이런식으로 프롬프트에 있는 내용만 조금 수정한다면 출력값을 바꿀수가 있다.

**Chat GPT랑 비교를 해보면**

![](./img/176_img_14.png)

이런식으로 대화 창 말고도 이미지 그리기 웹에서 검색하기 글쓰기 또는 코디 심층 리서치 등 정말 많은 서비스들이 존재한다.

하지만 GPT API 무료 버전이므로 정보자체가 2024년에 멈춰있다 그래서 검색엔진을 넣어서 최신 정보를 넣어줘야 하기 때문에 검색 엔진 API를 따로 받아서 설치해보겠습니다.

**검색 엔진 API**

* * *

<https://www.tavily.com/>

![](./img/176_img_15.png)

여기서 회원가입만 하면 API 키를 쉽게 받을 수 있다.

**구글 코랩으로 실습하기**

* * *

이번 AI는 검색엔진을 가지고 있는 AI라 최신 주가나 최신 뉴스를 가져올 수 있으므로 그에 걸맞게 

KOSPI 종목 투자 보고서 생성기 라는 AI를 가지고 실습해보겠다.

![](./img/176_img_16.png)

위 사진에서 보면 검색엔진을 사용해서 뉴스를 뽑아서 보고서를 작성하는걸 볼 수 있습니다.

이 것도 마찬가지도 위에 실습과 같이 코드를 수정을 해서 4번을 붙혀서 응답을 받을 수 있습니다.

**pdf파일 요약 AI**

* * *

![](./img/176_img_17.png)

이런식으로 pdf를 올리면 요약해주는 AI이다.

1\. PDF는 LLM이 바로 처리하기엔 너무 큽니다

  * PDF는 수십 페이지, 수천 단어가 될 수 있습니다.
  * LLM(OpenAI 등)은 토큰 한계가 있어서 한 번에 전체 내용을 넣을 수 없습니다.



넣는 방법
    
    
    import streamlit as st
    from langchain_community.document_loaders import PyPDFLoader
    from langchain.chains.combine_documents import create_stuff_documents_chain
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_openai import ChatOpenAI
    import tempfile
    import os

**LangChain**

* * *

LangChain은 대규모 언어 모델(LLM, Large Language Model)을 기반으로 한 애플리케이션을 더 쉽게 만들고 구성할 수 있도록 도와주는 프레임워크입니다. LangChain은 OpenAI의 ChatGPT 같은 LLM을 다양한 데이터 소스나 툴과 연결해서, 보다 복잡한 응용 프로그램을 만들 수 있도록 설계되었습니다.

이번엔 데이터를 저장하는 챗봇을 실습해보겠습니다, 여기서 데이터를 저장하는 이유는 LLM 구조상 기억을 하지 못하기 때문입니다. Chat GPT를 사용해보신 분이라면 새 채팅을 눌르면 GPT가 기억을 잃어버리는 걸 기억 하실 껍니다. LLM은 본질적으로 단일 입력 -> 단일 출력 구조라 이전 대화 내용을 스스로 저장하거나 참조하지 않습니다. 즉 GPT에 말을 걸면 그때 주어진 "프롬프트"만 보고 답을 만듭니다.

**chatbot 실습**

* * *

![](./img/176_img_18.png)

기억을 할 수 있게 하는 코드
    
    
    # 세션 상태에 대화 기록 저장
    if "messages" not in st.session_state:
        st.session_state.messages = []

**Ollama를 이용해서 LLM돌리기**

* * *

지금까지의 AI 실습 구조

대부분의 AI 실습은 아래처럼 구성되어 있었습니다:

  1. GPT API (예: OpenAI API)
  2. 검색엔진 API (예: Google Search API)



즉, 질문을 하면 클라이언트가 이들 외부 서비스로 요청을 보내고,  
그쪽 서버에서 처리된 결과를 응답으로 받는 구조였습니다.

이 방식의 한계

문제 | 설명  
---|---  
비용 | API 사용량이 늘수록 과금도 증가함 (토큰당 요금)  
외부 의존 | 인터넷 연결 필수, API 장애나 제한에 영향받음  
보안 문제 | 민감한 데이터를 외부 서버에 보내야 함  
폐쇄망 불가  | 군대, 연구소, 보안시설 같은 인트라넷 환경에서는 불가능  
  
대안은 있는가? → Ollama가 해결책

Ollama는 이런 문제를 해결해 줄 수 있는 로컬 LLM 실행 솔루션입니다.

항목 | 설명  
---|---  
완전 로컬 실행 | 인터넷 없이도 작동 가능 (인트라넷 환경 OK)  
무료 |  API 요금 없이 무료로 모델 사용 가능  
보안 보장  | 외부 전송 없음 -> 민감 정보 안전  
  
하지만 장점만 있는건 아닙니다. 다음은 단점입니다.

단점 | 설명  
---|---  
GPU 요구 | CPU도 가능하지만 느리고 제한적  
GPT-4보단 성능 낮음 | Mistral, LLaMA는 GPT-3.5 수준  
높은 자원 소모 | 모델당 수 GB, RAM도 많이 필요  
CLI 위주 | 설치/활용이 초보자에겐 진입장벽  
다중 사용자 불편 | 서버 배포 시 별도 구성 필요  
  
하지만 코랩으로 돌리면 구글 GPU를 사용할 수 있기때문에 ollama도 실습이 가능합니다.

**구글 코랩으로 실습하기**

* * *

<https://ollama.com/>

[ Ollama Get up and running with large language models. ollama.com ](https://ollama.com/)

1\. Google Colab은 리눅스 기반 가상 머신을 제공합니다

  * 코랩이 제공하는 노트북은 내부적으로 Ubuntu Linux 환경 위에서 돌아갑니다.
  * 즉, 우리가 Python 코드를 실행할 때, 실제로는 리눅스 셸에서 Python을 구동하고 있는 겁니다.



그래서 ollama 자체도 리눅스형태로 다운을 받고 코랩에서 구동시켜야한다 다음 사진은 터미널 실행 후 ollama설치, 시작한 화면입니다.

![](./img/176_img_19.png)

이건 ollama 가 제공하는 AI Library 입니다.

<https://ollama.com/library>

[ library Browse Ollama's library of models. ollama.com ](https://ollama.com/library)

이 중에 구글의 gemma3, LG의 exaone3.5 을 사용해보겠습니다.

다운로드한 모델 리스트 1.6GB,3.3GB입니다.

![](./img/176_img_20.png)

**exaone3.5**

* * *

"용인 벚꽃놀이 명소는 어딘가요?"

용인 벚꽃놀이 명소로는 다음 장소들을 추천드립니다:   
  
1\. **용인시 에버랜드 벚꽃길** - 에버랜드의 주요 산책로와 공원 내에서 아름다운 벚꽃을 감상할 수 있습니다. 특히 봄이 되면 화사한 꽃들이 펼쳐져 있습니다.   
  
2\. **용인 한택수지** - 이곳은 자연친화적인 환경 속에서 벚꽃을 만끽할 수 있는 최고의 장소 중 하나입니다. 넓은 숲 사이로 펼쳐지는 벚꽃길은 방문객들에게 평화로운 분위기를 선사합니다.   
  
3\. **용인원근 용인시청앞 벚꽃길** - 용인시청 주변의 벚꽃길은 접근성이 좋으며, 짧은 산책으로도 아름다운 자연 풍경을 즐길 수 있습니다. 특히 봄에 방문하면 생동감 넘치는 경치를 경험할 수 있습니다.   
  
이 외에도 다양한 공원이나 산책로에서도 벚꽃을 감상할 수 있으니, 현지의 공식 관광 정보나 지역 축제 웹사이트를 통해 더욱 자세한 정보를 얻어보시는 것도 좋습니다.

**gemma3:4b Model**

* * *

"용인 벚꽃놀이 명소는 어딘가요?"

용인에는 아름다운 벚꽃 명소들이 정말 많습니다! 몇 군데 추천해 드릴게요.   
  
**1. 신선류공원:**   
  
* **특징:** 용인에서 가장 넓은 규모를 자랑하며, 벚꽃 터널이 특히 유명합니다.   
* **규모:** 100헥타리 규모로 벚꽃이 전체적으로 화려하게 만개합니다.   
* **분수:** 멋진 분수와 함께 벚꽃을 즐길 수 있습니다.   
* **주소:** 경기도 용인시 처인구 포곡읍 신선로 147   
* **주차:** 유료, 5,000원   
  
**2. 용인 수정공원:**   
  
* **특징:** 오르막길을 따라 벚꽃길이 조성되어 있어 아름다운 풍경을 감상하기 좋습니다.   
* **분수:** 웅장한 분수와 함께 벚꽃을 즐길 수 있습니다.   
* **주소:** 경기도 용인시 처인구 성균관로 95   
* **주차:** 유료, 3,000원   
  
**3. 세류공원:**   
  
* **특징:** 벚꽃길과 함께 다양한 산책로가 잘 조성되어 있어 가볍게 산책하기 좋습니다.   
* **주소:** 경기도 용인시 처인구 세류로 117   
* **주차:** 유료, 3,000원   
  
**4. 용인서울매향공원:**   
  
* **특징:** 벚꽃과 함께 다양한 꽃과 식물을 감상할 수 있습니다.   
* **주소:** 경기도 용인시 처인구 상가로 77   
* **주차:** 유료, 3,000원   
  
**5. 기흥유원지:**   
  
* **특징:** 벚꽃과 함께 호수 주변을 산책하거나 자전거를 타며 여유로운 시간을 보낼 수 있습니다.   
* **주소:** 경기도 용인시 처인구 정자동 1   
* **주차:** 유료, 3,000원   
  
**팁:**   
  
* 벚꽃 개화 시기는 매년 조금씩 다르므로, 방문 전에 개화 상황을 확인하는 것이 좋습니다. (주로 4월 중순 이후)   
* 각 공원마다 주차 공간이 협소할 수 있으므로, 대중교통 이용을 고려하는 것이 좋습니다.   
* 돗자리, 간식 등을 챙겨 피크닉을 즐기는 것도 좋은 방법입니다.   
  
**참고 사이트:**   
  
* **용인시 문화관광 홈페이지:** [<https://www.yongin.go.kr/tour/tour_03_01.do](https://www.yongin.go.kr/tour/tour_03_01.do)>  
  
즐거운 벚꽃놀이 되세요!

확실히 gemma3:4b Model이 성능이 좋은거 같다.

이번엔 조금 어렵게 질문 해보겠습니다.

**Simple Chaine " | " (단일 체인)**

주어진 주제에 대해 초등학생도 이해할 수 있는 내용으로 설명하세요.

"topic": "양자컴퓨터"

자, 양자컴퓨터에 대해 알아볼까요? 마치 마법 상자 같은 아주 특별한 컴퓨터예요!   
  
**1. 평범한 컴퓨터는 '0' 아니면 '1'만 다룰 수 있어요.**   
  
* 우리가 쓰는 컴퓨터는 ‘0’ (꺼짐) 또는 ‘1’ (켜짐) 둘 중 하나의 숫자만 다룰 수 있어요. 마치 스위치를 켜거나 끄는 것과 같아요.   
* 이 ‘0’과 ‘1’를 모아서 복잡한 계산을 하지만, 여러 가지 숫자를 동시에 처리하는 건 어려워요.   
  
**2. 양자컴퓨터는 ‘0’과 ‘1’를 동시에 다룰 수 있어요!**   
  
* 양자컴퓨터는 ‘0’과 ‘1’를 동시에 다룰 수 있어요. 마치 동전 던지기처럼, 공중에서 앞면과 뒷면이 섞여 있는 상태를 이용하는 것과 비슷해요. 이걸 ‘양자 중첩’이라고 불러요.   
* 이렇게 동시에 여러 가지 가능성을 다룰 수 있어서, 엄청나게 복잡한 문제들을 훨씬 빠르게 풀 수 있어요.   
  
**3. 양자컴퓨터는 어떻게 작동할까요?**   
  
* 양자컴퓨터는 ‘큐비트(Qubit)’라는 특별한 것을 사용해요. 큐비트는 전자, 원자 같은 아주 작은 것을 이용해서 큐비트를 만들어요.   
* 큐비트는 위에 말한 것처럼 ‘0’과 ‘1’를 동시에 가지고 있을 수 있어요. 그리고 이 큐비트들이 서로 영향을 주고 받으면서 복잡한 계산을 해요.   
  
**4. 양자컴퓨터는 무엇을 할 수 있을까요?**   
  
* 양자컴퓨터는 아직 개발 중이지만, 미래에는…   
* 새로운 약을 개발하는 데 도움을 줄 수 있어요.   
* 아주 복잡한 금융 문제들을 해결하는 데 도움을 줄 수 있어요.   
* 새로운 소재를 개발하는 데 도움을 줄 수 있어요.   
* 그리고… 더 많은 것을 할 수 있을 거예요!   
  
**쉽게 말해서, 양자컴퓨터는 평범한 컴퓨터보다 훨씬 똑똑하고, 아주 어려운 문제들을 훨씬 빨리 풀 수 있는 컴퓨터라고 생각하면 돼요!**   
  
어때요? 좀 더 이해가 되나요? 혹시 더 궁금한 점이 있다면 언제든지 물어보세요! ?

**Simple Sequential Chain (연속 체인)**

{place}에서 맛집 3곳을 추천해주세요.

추천이 완료되면, 장소별로 방문자 2명의 예상 식사비용을 현지 통화로 예측해주세요.

그리고 현재 예산 {budget}과 비교하여 충분한지, 부족한지 확인해주세요. 주문에 필요한 현지어도 알려주세요.

"place": "시부야", "budget": "100,000원"

## 시부야 맛집 추천 및 예상 식사 비용 분석   
  
제공된 시부야 맛집 정보와 함께 예상 식사 비용을 분석하고, 주문에 필요한 현지어를 추가했습니다.   
  
**1. 스시 스즈키 (Sushi Suzuki)**   
  
* **특징:** 미슐랭 스타를 받은 고급 스시집.   
* **위치:** 도에이 신사마에 혼마치길 17-2   
* **가격대:** 1인당 약 8,000~15,000엔   
* **예상 방문자:** 2명   
* **예상 총 식사비:** 16,000 ~ 30,000엔   
* **현지어:** “お造り (ozashi)” (회), “おذا (oda)” (스시), “お勘定 (kan’tei)” (계산)   
  
**2. 하치코 (Hachiko)**   
  
* **특징:** 시부야 명물 핫도그.   
* **위치:** 시부야 1초메 모토즈구치스즈키다이구 1-2   
* **가격대:** 핫도그 600엔, 맥주 등 곁들임 메뉴 별도   
* **예상 방문자:** 2명   
* **예상 총 식사비:** 1,200엔 (핫도그) + 곁들임 메뉴 (예상 1,000엔) = 약 2,200엔   
* **현지어:** “ホットドッグ (hotto doggu)” (핫도그), “ビール (biiru)” (맥주), "お代物 (oya-bune)" (상징적인 음식)   
  
**3. 이마가와 (Imawa)**   
  
* **특징:** 츠루마미와 멘마의 맛집.   
* **위치:** 시부야 1초메 모토즈구치스즈키다이구 5-3   
* **가격대:** 츠루마미 300엔, 멘마 380엔   
* **예상 방문자:** 2명   
* **예상 총 식사비:** 1,500엔   
* **현지어:** “츠루마미 (tsurumamii)” (긴자빵), “メンマ (menma)” (조림), "おつまみ (otsumami)" (안주)   
  
**총 예상 식사 비용 (3곳):** 약 15,700엔   
  
**현지 통화:** 엔 (JPY)   
  
**예산 확인:**   
  
* 제공된 예상 식사 비용은 15,700엔이며, 이는 시부야에서 2명이 식사를 즐기기에 충분한 금액입니다. 하지만, 곁들임 메뉴를 추가하거나, 더 고급 레스토랑을 방문할 경우 예산이 초과될 수 있습니다.   
  
**추가 팁:**   
  
* **가상 화폐 (Bitcoin):** 일본에서는 일부 상점에서 비트코인도 사용할 수 있습니다.   
* **현금:** 현금 결제가 여전히 일반적이므로, 현금을 준비하는 것이 좋습니다.   
* **교환 서비스:** 환전은 공항이나 은행에서 가능합니다.   
  
즐거운 시부야 여행 되세요! 

**LLM (Large Language Model)**

* * *

**정의**

  * 대규모 텍스트 데이터를 학습하여 언어 이해, 생성, 요약 등 다양한 자연어 처리 작업을 수행할 수 있는 고성능 AI 모델



![](./img/176_img_21.png) https://arxiv.org/abs/2304.13712

2023년 상반기까지 LLM(대규모 언어 모델) 기술은 말 그대로 ‘Big Tech 리그’로 불릴 만큼 진입 장벽이 높았습니다.  
수십억에서 수백억 개의 파라미터를 가진 기초 모델(Foundation Model)을 연구하고 구축하기 위해서는 막대한 비용과 자원이 필요했으며,모델 아키텍처나 학습 데이터와 같은 핵심 정보는 대부분 비공개로 유지되었습니다.

하지만 Meta가 공개한 오픈소스 LLM인 LLaMA의 등장은 판도를 바꾸었습니다.  
이후 다양한 오픈소스 LLM 생태계가 주목받기 시작했으며,이제는 소형 모델도 대형 모델에 견줄 만큼 성능을 낼 수 있고,  
비교적 적은 데이터와 자원만으로도 파인튜닝(Fine-tuning)이 가능해졌습니다.즉, 오픈소스 LLM의 등장은 저비용·고효율의 LLM 활용 가능성을 현실로 만들고 있습니다.

![](./img/176_img_22.png) https://devopedia.org/llama-llm

2025년 6월 현재 

텍스트 생성 & 대화형 AI (LLM) 비교 및 순위

"Best in Reasoning (GPQA Diamond)"은 LLM 모델의 복잡한 추론 능력을 측정하는 대표적인 벤치마크 중 하나인 GPQA(Gaokao Professional Question Answering) Diamond 버전에서 최고 점수를 받은 모델을 의미합니다.

![](./img/176_img_23.png)

이용자 수론 당연 GPT가 압도적 1등이지만 성능 수준에서 구글이 더 좋은 걸 볼 수 있다 또한 이번 구글 I/O의 주인공이 Gemini였던걸 보면 Gemini가 곧 이용자수도 이길 수 있지않을까 생각해본다.

<https://www.youtube.com/live/o8NiE3XMPrM?si=YrNrzhwBwfEzeeF8>


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

**태그**: #대외활동생성형AI를활용한서비스콘텐츠제작
**상태**: 🌱 씨앗 (제텔카스텐 통합 대기)
**변환일**: 2025-10-07
