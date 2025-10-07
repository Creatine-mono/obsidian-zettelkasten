# GPT-4, Langchain 을 활용하여 AI 웹 서비스 만들기(2)

> **원본 포스트 ID**: 224
> **발행일**: 2025-07-17 01:06:51
> **카테고리**: project/웹개발

## 📝 원문 내용

**Large language model import 하기**

from langchain.llms import OpenAI

from langchain.chat_models import ChatOpenAI

OpenAI의 소스코드 중

client: Any = None #: :meta private:

model_name: str = Field(default="text-davinci-003", alias="model")

ChatOpenAI의 소스코드 중

if self.tiktoken_model_name is not None:

model = self.tiktoken_model_name

else:

model = self.model_name

if model == "gpt-3.5-turbo":

# gpt-3.5-turbo may change over time.

# Returning num tokens assuming gpt-3.5-turbo-0301.

model = "gpt-3.5-turbo-0301"

**둘의 차이점을 비교해보자**

![](./img/224_img.png) ![](./img/224_img_1.png)

이제한번 써봅시다 

llm = OpenAI(model_name="gpt-3.5-turbo-1106")

chat = ChatOpenAI(model_name="gpt-3.5-turbo")

  


a = llm.predict("Hello, how are you today?")

b = chat.predict("Hello, how are you today?")

  


a,b

**결과 화면**

![](./img/224_img_2.png)

여기서 에러가 난다면 

.env 파일에 API KEY 확인하기

OPENAI_API_KEY = sk-proj.......

꼭 이런식으로 되어야함

다른 옵션도 있음

llm = OpenAI(model_name="gpt-3.5-turbo-1106")

chat = ChatOpenAI(model_name="gpt-3.5-turbo")

여기 괄호안에 API키를 넣는 방법 하지만 .env파일에다가 넣는게 편합니다.

**Predict Messages**

from langchain.chat_models import ChatOpenAI

  


chat = ChatOpenAI(

temperature=0.1

)

앞서 보시다시피 괄호안에는 설정할수있는게 들어갑니다.

from langchain.schema import HumanMessage, AIMessage, SystemMessage

  


messages = [

SystemMessage(content="You are a friendly and concise language tutor. "),

AIMessage(content= "Use technical but understandable language suitable for a college student."),

HumanMessage(content="Can you explain the difference between BERT and GPT in simple terms?")

]

  


chat.predict_messages(messages)

**답변**
    
    
    AIMessage(content='Of course! BERT (Bidirectional Encoder Representations from Transformers) and GPT (Generative Pre-trained Transformer) are both advanced models used in natural language processing.\n\nThe main difference between BERT and GPT lies in their architecture and training objectives. BERT is designed for bidirectional learning, meaning it can understand the context of a word based on both the words that come before and after it. This allows BERT to capture more complex relationships within a sentence.\n\nOn the other hand, GPT is a unidirectional model that generates text based on the context it has seen so far. It excels at tasks like text generation and completion.\n\nIn summary, BERT focuses on understanding bidirectional context, while GPT is more geared towards generating text based on the context it has learned.')

**Prompt Templates**


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
