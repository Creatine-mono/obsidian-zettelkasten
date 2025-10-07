# GPT-4, Langchain 을 활용하여 AI 웹 서비스 만들기

> **원본 포스트 ID**: 222
> **발행일**: 2025-07-15 23:57:56
> **카테고리**: project/웹개발

## 📝 원문 내용

사용할 도구들

**LangChain**

<https://www.langchain.com/>

[ LangChain LangChain’s suite of products supports developers along each step of their development journey. www.langchain.com ](https://www.langchain.com/)

사용하는 이유

**랭체인**(LangChain)은 LLM(대형 언어 모델)을 사용하여 애플리케이션 생성을 단순화하도록 설계된 프레임워크이다. 언어 모델 통합 프레임워크로서 랭체인의 사용 사례는 문서 분석 및 요역, 챗봇, 코드 분석을 포함하여 일반적인 언어 모델의 사용 사례와 크게 겹친다.

**Streamlit**

<https://streamlit.io/>

[ Streamlit • A faster way to build and share data apps Streamlit is an open-source Python framework for data scientists and AI/ML engineers to deliver interactive data apps – in only a few lines of code. streamlit.io ](https://streamlit.io/)

**사용하는 이유**

  * Python 기반의 오픈 소스 라이브러리
  * Python 스크립트를 통해 데이터 시각화, 대화형 웹 애플리케이션, 대시보드 등을 손쉽게 만들 수 있음
  * 공식 사이트에서는 "A faster way to build and share data apps"라고 말하며, 데이터 애플리케이션을 구축하고 공유하는 가장 빠른 방법을 제공한다고 함
  * 웹사이트 구축에 프론트엔드적 경험이 불필요함



**Pinecone**

<https://www.pinecone.io/>

[ The vector database to build knowledgeable AI | Pinecone Search through billions of items for similar matches to any object, in milliseconds. It’s the next generation of search, an API call away. www.pinecone.io ](https://www.pinecone.io/)

**GPT-4**

[https://openai.com/](https://openai.com/ko-KR/index/gpt-4/)

![](./img/222_download.png)

**Hugging face**

<https://huggingface.co/>

[ Hugging Face – The AI community building the future. The Home of Machine Learning Create, discover and collaborate on ML better. We provide paid Compute and Enterprise solutions. We are building the foundation of ML tooling with the community. huggingface.co ](https://huggingface.co/)

**Fast API**

<https://fastapi.tiangolo.com/ko/>

[ FastAPI FastAPI framework, high performance, easy to learn, fast to code, ready for production fastapi.tiangolo.com ](https://fastapi.tiangolo.com/ko/)

**요구조건**

ChatGPT plus의 유료 구독자야만함

**Virtual Environment**

![](./img/222_img.png)

파일을 하나 생성한다.

git 터미널을 키고난 후 명령어를 쳐준다
    
    
    python -m venv ./env

![](./img/222_img_1.png) ![](./img/222_img_2.png)

이러면 커밋이 난리가 나니까 미리 생성해둔 .gitignore 파일에 업로드를 안하게 하는 명령어를 넣놓자

env/

<https://docs.python.org/3/library/venv.html>

[ venv — Creation of virtual environments Source code: Lib/venv/ The venv module supports creating lightweight “virtual environments”, each with their own independent set of Python packages installed in their site directories. A virtual en... docs.python.org ](https://docs.python.org/3/library/venv.html)

이제 이페이지에서 윈도우환경에서 가상환경에 접속하는법 맥,리눅스 모두써있으니 참고해보자

![](./img/222_img_3.png)

앞에 (env)가 뜸으로써 잘 들어가졌다는걸 알 수 있다.

requirements.txt파일에 설치할 파일들을 적어놓은 다음 설치를 진행해보자
    
    
    pip install -r requirments.txt

**터미널에서 경로를 못찾는 경우**

명시적인 경로로 가상환경 생성
    
    
    "/c/Users/박성호꺼/AppData/Local/Programs/Python/Python311/python.exe" -m venv env

다운로드 해가는 과정

![](./img/222_img_4.png)

이제 설치가 잘되었는지 확인해봅시다.

main.py파일 생성

생성후 

import tiktoken

  


print(tiktoken)

하고 터미널에서 확인

![](./img/222_img_5.png)

설치가 잘되었음을 확인 할 수 있다.
    
    
    deactivate

이 명령어를 사용하면 가상환경에서 나올 수 있는데 우리는 설치가 가상환경에서 잘 되었는지 확인하고 싶은거기 때문에 나와서도 확인을 해야한다.

이제 Virtual envirment variable 들을 넣을 파일 생성해주자

.env

![](./img/222_img_6.png)

API key나 보안유지가 필요한것들을 넣는 공간이다.

그러므로 gitignore 파일에도 추가해주자

#### **Jupyter Notebooks 배워보기**

![](./img/222_img_7.png)

확장자가 ipynb인 파일 생성해주기

생성이 완료되었다면 제일먼저 커널을 선해주는거다

![](./img/222_img_8.png) ![](./img/222_img_9.png)

이제 가상환경에 다운받은 모든 것들을 여기서 실행할 수 있다.

만약 커널선택에서 안보이면 Jupyter 익스텐션 다운받기!!

**주피터를 사용하는이유**

![](./img/222_img_10.png)

보시다시피 c만 적어도 출력이된다.

또한 코드실행되고 다른 셀로 바껴도 값은 보존된다.


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
