# LLM Guard와 Microsoft Presidio를 활용한 보안 중심 AI 시스템 구축

## 전체 시스템 구성: 입력 필터링 → Gemini API 호출 → 출력 필터링

보안 강화를 위한 AI 시스템은 사용자 입력을 전처리(필터링)하고, 그 후 LLM 모델(Gemini)을 호출하여 응답을 생성하며, 최종적으로 출력 결과를 다시 필터링**하는 단계로 구성됩니다. 이렇게 다단계 **미들웨어**를 두어야만 외부 LLM에 보내는 데이터 및 LLM이 생성한 응답 모두가 안전하게 관리됩니다. 시스템 흐름은 다음과 같습니다:

1. **입력 필터링 단계:** 사용자가 입력한 프롬프트를 수신하면 우선 **LLM Guard**와 **Presidio**를 이용해 내용 점검 및 정제가 이루어집니다. 이 단계에서는 프롬프트에 **금지된 내용이나 악성 패턴**이 포함되어 있는지 탐지하고 제거하거나, 정책상 허용되지 않는 경우 요청 자체를 거부합니다. 또한 **이메일 주소나 전화번호** 등의 개인 식별 정보(PII)를 식별하여 마스킹 처리합니다. 이러한 입력 단계의 **철저한 검증과 정제**를 통해 LLM이 **유해하거나 민감한 정보에 노출되지 않도록** 합니다.
    
2. **Gemini LLM 호출:** 필터링된 안전한 입력만이 **Google DeepMind의 Gemini 모델** API로 전달됩니다. Gemini는 멀티모달 지원이 가능한 최신 LLM으로, 주어진 프롬프트에 대한 답변을 생성합니다. 이때 모델 호출은 Google Cloud의 Vertex AI 상의 Gemini API를 사용하며, **API 키 인증**을 거쳐 **지정한 모델** (예: `gemini-2.5-flash`나 `gemini-1.5-pro`)에 텍스트를 전달해 응답을 받게 됩니다.
    
3. **출력 필터링 단계:** Gemini로부터 생성된 응답에 대해서도 **LLM Guard**와 **Presidio** 기반의 **후처리 필터**가 적용됩니다. 모델 출력에 **비속어, 편향된 표현, 민감 데이터** 등이 포함되었는지 검열하고 필요시 해당 내용을 제거하거나 수정합니다. 또한 모델이 **사용자 입력에 포함되었던 PII를 응답에 포함하거나 누설**하지 않도록 검증하며, 앞서 마스킹했던 플레이스홀더는 필요에 따라 원본 정보로 복원할 수도 있습니다. 이러한 출력 필터링을 통해 **최종적으로 사용자에게 전달되는 답변이 정책에 부합하고 안전한지**를 한 번 더 확인합니다.

요약하면, **입력** -> **(LLM Guard & Presidio 필터)** -> **Gemini 응답 생성** -> **(LLM Guard & Presidio 필터)** -> **출력**의 파이프라인을 거침으로써, **모델 상호작용 전 과정에서 보안과 프라이버시를 보장**하게 됩니다.

## LLM Guard를 통한 입력 필터링 및 프롬프트 보호

**LLM Guard**는 Protect AI에서 개발한 **LLM 보안 툴킷**으로, **프롬프트 단계의 다양한 위험을 선제적으로 탐지하고 차단**합니다. LLM Guard를 활용하면 다음과 같은 주요 기능을 구현할 수 있습니다.

- **Prompt Injection 탐지:** Prompt Injection은 사용자가 의도적으로 `'이전 지시를 무시하고 ...'` 등의 구문을 넣어 **모델의 시스템/정책 지시를 무력화**하려는 공격입니다. LLM Guard는 이런 **프롬프트 인젝션 패턴**을 미리 정의된 스캐너로 식별하여 경고하거나 차단합니다. 예를 들어 **`PromptInjection()`** 스캐너를 통해 프롬프트에 **시스템 명령 무시, 차별 조장 문구, 숨겨진 인비저블 텍스트** 등이 있는지 검사할 수 있습니다. 인젝션 시도가 발견되면 해당 부분을 삭제하거나 요청을 거부함으로써 **LLM의 의도치 않은 오남용**을 방지합니다.
    
- **유해 키워드 및 주제 차단:** LLM Guard는 미리 정의한 **금지 단어 목록**이나 **주제 필터**를 적용하여 **악의적이거나 부적절한 내용**을 탐지할 수 있습니다. 예를 들어 **폭력, 증오, 불법 활동** 등 금지된 토픽이 포함되면 **`BanTopics`** 또는 **`BanSubstrings`** 스캐너가 이를 감지하여 해당 프롬프트를 **유효하지 않은 것으로 판정**합니다. 또한 **욕설이나 혐오 표현**에 대해서는 **Toxicity 스캐너**로 **유해성을 점수화**하여 기준치 이상일 경우 차단할 수 있습니다. 이러한 **콘텐츠 필터링**을 통해, 사용자의 악의적 요청이나 부적절한 요구사항이 LLM에 전달되지 않도록 합니다.
    
- **프롬프트 정제(Sanitization):** LLM Guard는 입력 프롬프트를 **더 안전하고 표준화된 형태로 교정 및 정제**해줄 수도 있습니다. 예를 들어 프롬프트에 **제어 문자나 보이지 않는 특수문자(Invisible Text)**가 숨겨져 있다면 이를 제거하고, **너무 긴 프롬프트**의 경우 **TokenLimit 스캐너**를 통해 일정 토큰 수 이후를 잘라낼 수 있습니다. 또한 LLM Guard에는 **`Anonymize`** 스캐너가 내장되어 있어 프롬프트 내 **전화번호, 이메일** 등의 **민감 정보를 자동으로 치환**하는 기능도 제공합니다. (이 `Anonymize` 스캐너는 감지된 PII를 `<IDENTIFIER>` 형태의 토큰으로 바꾸고 안전하게 보관하기 때문에, 이후 모델 응답에서 해당 토큰을 원본 값으로 **복원(Deanonymize)하는 것도 가능합니다.) 이러한 정제 과정을 통해 데이터 누출 방지와 입력 클린싱**이 이루어지며, LLM에는 **오직 필요한 정보만 전달**됩니다.
    

LLM Guard의 이러한 스캐너들은 개별적으로 사용할 수도 있고, 한 번에 조합하여 적용할 수도 있습니다. 예를 들어 여러 필터를 조합하여 한꺼번에 프롬프트를 검사하려면 다음과 같이 사용합니다.

```python
```python
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

analyzer = AnalyzerEngine()               # PII 분석 엔진 초기화
anonymizer = AnonymizerEngine

```
```python

from llm_guard import scan_prompt from llm_guard.input_scanners import PromptInjection, BanTopics, Toxicity, TokenLimit  input_scanners = [     PromptInjection(),                    # 프롬프트 인젝션 패턴 감지     BanTopics(topics=["폭력", "혐오"]),    # 지정된 유해 주제 차단     Toxicity(threshold=0.5),             # 독성 내용 점수화 (예시로 임계값 0.5)     TokenLimit(max_tokens=1000)          # 토큰 길이 제한 (예: 1000토큰 초과 시 잘라냄) ]  sanitized_prompt, results_valid, results_score = scan_prompt(input_scanners, prompt) if any(not valid for valid in results_valid.values()):     raise ValueError("입력에 허용되지 않는 내용이 감지되어 중단되었습니다.")`
```
```

위와 같이 `scan_prompt` 함수에 여러 스캐너를 전달하면, 입력 프롬프트에 대한 정제된 버전(`sanitized_prompt`)과 함께 각 검사별 유효 여부(`results_valid`) 및 위험 점수(`results_score`)가 반환됩니다. 한 가지라도 `results_valid`가 False인 검사가 있다면 해당 입력은 정책에 어긋나는 것으로 판단하여 처리 중단 또는 사용자에게 에러를 반환할 수 있습니다. 이처럼 LLM Guard 단계에서 문제 소지가 있는 입력은 미리 걸러지거나 수정되므로, Gemini 모델에는 안전한 프롬프트만 전달되게 됩니다.

## PII 탐지 및 마스킹: Microsoft Presidio 통합

LLM Guard의 기본 기능 외에, 개인정보(PII)에 특화된 정교한 탐지/마스킹 도구인 Microsoft Presidio를 함께 사용하여 보안을 한층 강화할 수 있습니다. Presidio는 오픈소스 PII 식별 및 익명화(anonymization) 프레임워크로, 텍스트 내에서 이메일, 전화번호, 신용카드 번호 등 다양한 개인 식별자를 자동으로 탐지하고 마스킹해줄 수 있습니다[ploomber.io](https://ploomber.io/blog/pii-openai/#:~:text=,anonymized).

![https://ploomber.io/blog/pii-openai/](blob:https://chatgpt.com/b2331330-c4d4-492d-918c-85c5d82d554c)

그림 1: PII 필터링 프록시 아키텍처 예시. 사용자가 챗봇에 “Show me the latest invoices for the customer with email peter.doe@corporation.com”과 같이 이메일 주소를 포함한 요청을 보낸 경우, 미들웨어 서버는 해당 입력을 가로채어 `peter.doe@corporation.com`을 `<EMAIL ADDRESS>`토큰으로 대체한 후 LLM에 전달합니다. 이로써 LLM은 실제 이메일 정보를 알지 못한 채 요청을 처리하게 되며, 응답 생성 시에도 이메일 주소 대신 플레이스홀더가 사용됩니다. 하단의 두 번째 예에서도, “...I’ve tried reaching out to 212-555-5555”라는 전화번호가 포함된 문장이 `<PHONE NUMBER>`로 치환된 것을 볼 수 있습니다. 이러한 프록시 구조를 통해 사용자 입력의 민감 정보가 외부 LLM에 직접 노출되는 것을 방지하고, 나아가 모델의 응답에서도 개인정보가 드러나지 않도록 제어할 수 있습니다.

Presidio의 동작 방식은 다음 두 단계로 이루어집니다: (1) PII 엔티티 탐지와 (2) 마스킹/치환입니다. 우선 `AnalyzerEngine`이 텍스트를 스캔하여 이메일 주소(`EMAIL_ADDRESS`), 전화번호(`PHONE_NUMBER`) 등 민감 정보 패턴을 인식합니다. 내장된 정규식 패턴과 ML 모델을 활용하여 입력 문자열과 일치하는 PII의 시작/끝 위치, 유형, 신뢰 점수 등을 결과로 반환합니다. 다음으로 `AnonymizerEngine`을 사용해 탐지된 위치의 텍스트를 마스킹 처리합니다[ploomber.io](https://ploomber.io/blog/pii-openai/#:~:text=,anonymized). 기본 설정으로는 이메일이나 전화번호 같은 엔티티를 각각 `<EMAIL_ADDRESS>`, `<PHONE_NUMBER>`와 같은 placeholder로 교체해주는데, 마스킹 방식은 커스터마이징도 가능합니다 (예: `*`로 덮어쓰거나 특정 문자열로 대체 등).

예를 들어 Presidio를 사용하여 이메일 주소와 전화번호를 식별 및 마스킹하는 파이썬 코드는 다음과 같습니다:

```python
```
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

analyzer = AnalyzerEngine()               # PII 분석 엔진 초기화
anonymizer = AnonymizerEngine

```


위 코드에서는 `AnalyzerEngine`으로 이메일 주소와 전화번호 엔티티를 탐지한 후, `AnonymizerEngine`을 통해 이메일은 `<EMAIL>`로 **대체**하고, 전화번호는 뒷자리 4글자를 남긴 채 나머지는 `*`로 **마스킹**했습니다. Presidio를 사용하면 이처럼 민감 정보를 다양하게 가공할 수 있으며, **기본값으로 사용하는 경우 이메일 `john.doe@example.com`은 `<EMAIL_ADDRESS>`로 자동 치환**되는 등 편리한 설정도 제공됩니다[ploomber.io]. 실제로 앞서 도입한 프록시 예시에서도 Presidio를 통해 원본 요청의 이메일이 `<EMAIL_ADDRESS>` 토큰으로 바뀌었음을 확인할 수 있습니다.

본 시스템에서는 **입력단에서** Presidio를 활용하여 **사용자 프롬프트 내의 PII를 제거 또는 마스킹**하고, 나아가 **출력단에서도** 혹시 모를 PII 유출이 있는지 한번 더 확인할 수 있습니다. 특히 입력 단계에서 PII를 치환해둠으로써 Gemini와 같은 외부 모델에는 **민감한 원본 정보가 전달되지 않도록** 하며, 이를 통해 기업 내부 정책 준수 및 개인정보 보호 규정(GDPR, HIPAA 등) 위반 소지를 사전에 차단합니다. 또한 LLM Guard의 Vault 기능과 결합하면, 마스킹한 원본 정보를 Vault에 안전하게 저장해두었다가 **최종 사용자에게 응답을 반환하기 전 해당 위치에 실제 값을 복원**하는 것도 가능합니다. (예: 출력에서 `<PHONE_NUMBER>`가 있다면 Vault에 보관된 실제 번호 `010-1234-5678`로 되돌려주는 방식). 이러한 통합 기법을 통해 **모델에게는 개인정보를 숨기면서도, 사용자에게는 자연스러운 답변**을 제공할 수 있습니다.

## Gemini API 호출 방식 예시 (Python)

**Gemini API**는 Google Cloud Vertex AI의 일부로 제공되며, Python에서는 **Google GenAI SDK** (`google-genai` 라이브러리)를 사용하여 쉽게 호출할 수 있습니다. 먼저 Google AI Studio를 통해 **API 키**를 발급받아 환경변수 또는 코드 내에 설정한 뒤, 아래와 같은 코드로 Gemini 모델에 질의를 보낼 수 있습니다:

```
```python

`from google import genai  API_KEY = "발급받은-나의-API키" client = genai.Client(api_key=API_KEY)   response = client.models.generate_content(     model="gemini-2.5-flash",      contents="인공지능이 작동하는 원리를 간단히 설명해줘." ) print(response.text)`
```
```

위 코드에서는 `genai.Client`를 생성하면서 API 키를 지정하고, `generate_content` 메서드로 **Gemini 2.5 Flash 모델**에게 프롬프트를 전달하고 있습니다[ai.google.dev](https://ai.google.dev/gemini-api/docs/quickstart#:~:text=from%20google%20import%20genai). `model` 파라미터에는 사용할 모델의 이름(버전)을 지정하며, `contents`에 질의할 문자열을 넣습니다. 호출 결과는 `response.text`로 받아볼 수 있고, 여기에는 Gemini가 생성한 답변이 문자열로 담겨 있습니다. 예를 들어 위 요청은 _"인공지능이 작동하는 원리를 간단히 설명해줘."_ 라는 질문에 대한 답변을 반환할 것입니다.

Gemini API는 여러 등급의 모델(예: Nano, Pro, Ultra 등)과 여러 버전을 제공하므로, 목적에 맞게 모델을 선택할 수 있습니다. 또한 API 호출 시 온프레미스 OpenAI API와 유사한 방식으로 동작하기 때문에, 프롬프트만 준비되어 있다면 위와 같은 코드 한두 줄로 간단히 LLM 응답을 획득할 수 있습니다. (Google Cloud의 사전 설정과 키 설정이 완료되어야 함을 유의하십시오.) 더 복잡한 사용 사례로, 하나의 요청에 다수의 응답(candidate)을 받고 점수를 비교하거나, 함수 호출 기능을 활용하는 것도 Gemini API에서 가능합니다[datacamp.com]. 여기서는 단순한 텍스트 생성 요청 예시를 보여주었지만, 필요에 따라 다양한 옵션을 조정하여 사용할 수 있습니다.

#전체 통합 미들웨어 코드 예시 (FastAPI)

이제 앞서 설명한 모든 구성요소(LLM Guard, Presidio, Gemini API 호출)를 하나의 서버 애플리케이션으로 통합하는 예시를 소개합니다. 아래 코드는 Python의 FastAPI 프레임워크를 이용해 간단한 REST API 엔드포인트를 구현한 것입니다. 사용자가 `/chat` 경로로 질문을 보내면, 우리 미들웨어가 입력 필터링 → LLM 응답 생성 → 출력 필터링의 과정을 수행한 뒤 최종 답변을 반환합니다:

```
```python


`from fastapi import FastAPI, Request, HTTPException from llm_guard import scan_prompt, scan_output from llm_guard.input_scanners import PromptInjection, BanTopics, Toxicity from llm_guard.output_scanners import Sensitive, Toxicity as OutToxicity from presidio_analyzer import AnalyzerEngine from presidio_anonymizer import AnonymizerEngine from google import genai  # --- 1. 초기화: 필터 엔진들과 LLM 클라이언트 설정 --- app = FastAPI() # LLM Guard 스캐너 설정 (입력용과 출력용) input_scanners = [PromptInjection(), BanTopics(topics=["범죄", "폭력"]), Toxicity()] output_scanners = [Sensitive(), OutToxicity()] # Presidio 엔진 초기화 analyzer = AnalyzerEngine() anonymizer = AnonymizerEngine() # Gemini API 클라이언트 초기화 API_KEY = "YOUR_GEMINI_API_KEY"  # 실제 API 키로 설정 client = genai.Client(api_key=API_KEY)    # --- 2. 엔드포인트 정의 --- @app.post("/chat") async def chat(request: Request):     data = await request.json()     user_prompt = data.get("message")  # 사용자가 보낸 메시지          # 2-1. 입력 필터링: LLM Guard로 유해 내용 및 Injection 검사     sanitized_prompt, results_valid, _ = scan_prompt(input_scanners, user_prompt)     if any(not valid for valid in results_valid.values()):         raise HTTPException(status_code=400, detail="입력에 허용되지 않는 내용이 포함되었습니다.")     # 2-2. 입력 필터링: Presidio로 PII 탐지 및 마스킹     analyze_results = analyzer.analyze(text=sanitized_prompt, language='en')     sanitized_prompt = anonymizer.anonymize(text=sanitized_prompt, analyzer_results=analyze_results).text          # 2-3. LLM (Gemini) API 호출하여 응답 생성     try:         llm_response = client.models.generate_content(model="gemini-2.5-flash", contents=sanitized_prompt)     except Exception as e:         raise HTTPException(status_code=500, detail=f"Gemini API 오류: {e}")     answer_text = llm_response.text          # 2-4. 출력 필터링: LLM Guard로 응답 내용 점검     filtered_answer, out_results_valid, _ = scan_output(output_scanners, sanitized_prompt, answer_text)     if any(not valid for valid in out_results_valid.values()):         # 응답에 민감하거나 부적절한 내용이 있을 경우         filtered_answer = "[안전 필터링됨] " + filtered_answer  # 간단히 표시 후 통과 (또는 내용 제거 가능)     # 2-5. 출력 필터링: Presidio로 최종 PII 마스킹 확인     out_analyze_results = analyzer.analyze(text=filtered_answer, language='en')     final_answer = anonymizer.anonymize(text=filtered_answer, analyzer_results=out_analyze_results).text          # 최종 응답 반환     return {"answer": final_answer}`
```
```

위 FastAPI 미들웨어 예시는 전체 파이프라인을 한데 결합한 것입니다. 먼저 (1) 초기화 부분에서 LLM Guard의 입력/출력 스캐너 목록을 설정하고, Presidio 분석기와 익명화기를 생성하며, Gemini API를 호출하기 위한 클라이언트를 초기화합니다.

다음으로 (2) `/chat` 경로의 엔드포인트 함수에서는 다음 순서로 로직이 실행됩니다:

- 2-1단계: `scan_prompt`를 사용하여 LLM Guard 입력 스캐너들을 적용함으로써 사용자 `message`에 유해하거나 금지된 내용, prompt injection 시도가 있는지 검사합니다. 설정된 모든 스캐너(예에서는 PromptInjection, BanTopics, Toxicity)를 거친 후 하나라도 `valid` 값이 False이면 정책 위반으로 간주하여 HTTP 400 에러를 발생시킵니다. 이 단계에서 통과하면 `sanitized_prompt`에는 필요 시 일부 정제가 적용된 (예: 금지 주제가 별표 처리되거나 하는 등) 프롬프트가 들어 있습니다.
    
- 2-2단계: `AnalyzerEngine`으로 프롬프트 내 PII를 식별하고, `AnonymizerEngine`으로 이를 마스킹합니다. 여기서는 기본 동작을 사용했으므로 이메일, 전화번호 등이 자동으로 `<EMAIL_ADDRESS>`, `<PHONE_NUMBER>` 형태로 치환됩니다. 이 과정을 통해 민감한 정보가 제거된 최종 프롬프트(`sanitized_prompt`)를 얻게 됩니다.
    
- 2-3단계: 정제된 프롬프트를 가지고 Gemini API를 호출합니다. `generate_content` 메서드로 모델 이름과 내용을 전달하면 LLM이 응답을 생성하며, 실패 시 예외를 처리합니다. 성공하면 `answer_text` 변수에 모델의 원시 응답 내용이 저장됩니다.
    
- 2-4단계: LLM Guard의 출력 스캐너들을 이용해 모델 응답에 대한 검열을 수행합니다. 예시에서는 Sensitive 스캐너(민감한 내용 탐지)와 Toxicity 스캐너(출력 독성 여부 검사)를 적용하였습니다. 만약 응답에 민감정보(예: 개인정보, 기밀 등)가 그대로 포함되거나 부적절한 표현이 있다면 `results_valid` 중 해당 항목이 False가 될 것입니다. 이때는 `filtered_answer` 내용을 조정할 수 있습니다. 본 예에서는 간단히 `[안전 필터링됨]`이라는 라벨을 붙였지만, 필요하다면 문제되는 문장을 제거하거나 사전 정의한 안전 답변으로 교체할 수도 있습니다.
    
- 2-5단계: 최종으로 Presidio를 한 번 더 적용하여 출력에 혹시 남아있을지 모르는 PII를 마스킹합니다. (예: 모델이 새로운 이메일 주소를 생성하여 답변했다면 그것도 `<EMAIL_ADDRESS>`로 치환될 것입니다.) 이렇게 이중으로 확인함으로써 출력 단계에서도 개인정보 유출 가능성을 최소화합니다. 이후 `final_answer`를 JSON 형태로 클라이언트에 반환하면 한 사이클이 완료됩니다.
    

이 전체 흐름을 통해 클라이언트 측에서는 일반 OpenAI/Gemini API를 사용하고 질의하고 응답을 받지만, 실제로는 미들웨어가 그 사이에서 프록시 역할을 수행하며 모든 입력과 출력을 안전하게 관리하는 것입니다. 각 구성 요소는 필요에 따라 확장하거나 조절할 수 있습니다. 예를 들어 금지 주제 목록을 추가하거나, 사용자별로 다른 필터 정책을 적용할 수도 있고, Presidio의 마스킹 방식을 특정 형식(예: <USER_ID>)으로 변경할 수도 있습니다. 중요한 것은 이러한 미들웨어 레이어를 둠으로써 LLM을 서비스에 활용하면서도 보안 통제와 규제 준수를 달성할 수 있다는 점입니다.

개인정보반 발표 