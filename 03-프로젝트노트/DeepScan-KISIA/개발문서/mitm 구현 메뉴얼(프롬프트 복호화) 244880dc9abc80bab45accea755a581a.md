# mitm 구현 메뉴얼(프롬프트 복호화)

---

<aside>
💡

보안정책 강화되면 CA인증서 사용못할 수 있으니,

**플젝 끝날때까지 외부 유출(Github, Velog) 금지**

</aside>

# 1. 이론

테스트버전 (백업용)

[mitm_modulation.py](mitm_modulation.py)

[https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)   → exe파일 설치

```bash
# 설치되었는지 확인
tesseract --version
```

```bash
pip install chardet
pip install pymupdf
pip install pytesseract
pip install pillow
```

mitm_modulation.py에서 “SAVE_DIR” 자기 경로에 맞게 입력

```bash
mitmdump -s (파이썬파일경로) --set console_eventlog_verbosity=debug ƒ tee /tmp/mitm.log
```

아직 안썼음

추강민 화이팅

화이팅~~

우린 다했지롱

---

# 2. 구현

## ✅ 반드시 firefox로 실행할것

❌ **Chrome,safari** …은 HSTS 보안 정책에 따라 차단되어있다

### 1. 루트 CA 인증서 생성

1.1 루트 CA 생성

: 4096비트 RSA개인키 생성

```bash
openssl genrsa -out rootCA.key 4096
```

1.2 루트 CA 인증서 생성(자체 서명)

```bash
openssl req -x509 -new -nodes -key rootCA.key -sha256 -days 3650 -out rootCA.pem \
  -subj "/C=KR/ST=Seoul/L=Seoul/O=MyProxyRootCA/OU=Proxy/CN=MyProxyRootCA"
```

```bash
#윈도우
openssl req -x509 -new -nodes -key rootCA.key -sha256 -days 3650 -out rootCA.pem -subj "/C=KR/ST=Seoul/L=Seoul/O=MyProxyRootCA/OU=Proxy/CN=MyProxyRootCA"

```

### 2. 중간자 CA 인증서 생성

2.1 중간자 CA생성

```bash
openssl genrsa -out mitmproxyCA.key 4096
```

2.2 CSR생성(인증서 서명 요청)

```bash
openssl req -new -key mitmproxyCA.key -out mitmproxyCA.csr \
  -subj "/C=KR/ST=Seoul/L=Seoul/O=MyProxyCA/OU=Proxy/CN=MyProxyCA"
```

```bash
#윈도우
openssl req -new -key mitmproxyCA.key -out mitmproxyCA.csr -subj "/C=KR/ST=Seoul/L=Seoul/O=MyProxyCA/OU=Proxy/CN=MyProxyCA"

```

2.3 텍스트 편집기로 openssl 확장 설정 파일 만들기

```bash
nano rootCA.cnf
```

```bash
#윈도우
code rootCA.cnf
```

2.4 중간자 CA 인증서 서명(루트 CA로 서명)

```bash
[ v3_ca ]
basicConstraints = CA:TRUE
keyUsage = critical, digitalSignature, cRLSign, keyCertSign
subjectKeyIdentifier=hash
authorityKeyIdentifier=keyid:always,issuer
```

2.5 서명 명령

```bash
openssl x509 -req -in mitmproxyCA.csr -CA rootCA.pem -CAkey rootCA.key -CAcreateserial \
  -out mitmproxyCA.pem -days 1825 -sha256 -extfile rootCA.cnf -extensions v3_ca
```

```bash
#윈도우
openssl x509 -req -in mitmproxyCA.csr -CA rootCA.pem -CAkey rootCA.key -CAcreateserial -out mitmproxyCA.pem -days 1825 -sha256 -extfile rootCA.cnf -extensions v3_ca
```

### 3. 중간자 CA 인증서와 개인키를 합쳐서 프록시에서 사용할 파일 만들기

```bash
cat mitmproxyCA.pem mitmproxyCA.key > mitmproxyCA.pem.key.pem
```

```bash
#윈도우
type mitmproxyCA.pem mitmproxyCA.key > mitmproxyCA.pem.key.pem
```

### 4. 프록시 설정에 CA 등록 및 신뢰

1. **클라이언트(사용자 OS/브라우저)에 루트 CA 인증서(rootCA.pem)를 신뢰된 루트 인증서로 등록**
    - Windows: 인증서 관리 도구 (certmgr.msc)에서 루트 인증서 저장소에 추가
    - macOS: 키체인 접근 → 시스템 → 인증서에 추가 후 신뢰 설정
    - Linux: 각 배포판별 CA 신뢰 저장소에 추가 (예: /usr/local/share/ca-certificates/ 추가 후 `update-ca-certificates`)
2. **mitmproxy 또는 Burp Suite에 mitmproxyCA.pem.key.pem 파일을 프록시 CA로 설정**
    - mitmproxy 예: `-cert` 옵션으로 설정 가능하거나 mitmproxy 자체 생성 CA를 교체 가능
    - Burp Suite: 설정 → Proxy → Options → Import CA Cert (여기에 PEM 파일 추가)

### 4.3 생성한 루트 CA 신뢰 등록 방법

1. **Windows 루트 CA 신뢰 등록하기**

```bash
cp rootCA.pem rootCA.crt
```

- `rootCA.crt` 파일을 더블클릭하면 "인증서" 창이 뜹니다.
- 하단의 "인증서 설치" 버튼 클릭
- "로컬 컴퓨터" → "신뢰할 수 있는 루트 인증 기관" 저장소 선택
- 설치 마법사 완료 후 재부팅 없이도 적용됩니다.

**2. macOS에 루트 CA 신뢰 등록하기**

⚠️ 키체인 접근에 등록하면 **“myproxyrootCA”**라고 뜸

1. `rootCA.pem` 파일을 더블클릭하면 키체인 접근 앱이 열립니다.
2. `시스템` 키체인 선택 (또는 `로그인` 키체인)
3. "인증서" 항목에 `MyProxyRootCA` 같은 이름으로 등록됨
4. 등록된 인증서를 더블클릭 → "신뢰" 펼치기 → "이 인증서 사용 시:" → "항상 신뢰"로 변경
5. 관리자 암호 입력 후 종료

2.1 Mac에서 파일 위치 찾는 법

```bash
pwd
ls rootCA.pem
```

⚠️ 없으면 `ls: cannot access rootCA.pem: No such file or directory` 같은 메시지 뜸

시스템 전체 검색

```bash
find ~ -name rootCA.pem
```

1. mitmproxy에 중간자 CA pem 파일을 mitmproxy 폴더에 복사

```bash
mitmproxy --cert mitmproxyCA.pem.key.pem
```

해당 명령어를 실행하면 flows가 열릴 것임. **mitm이 정상적으로 작동한다면 로그가 뜬다**

1. 로그가 200Ok 로 뜨는것이 확인된다면, 다음 파이썬 파일을 다운로드하여 명령어를 다시 입력해보자. 입력한 프롬프트가 뜰것이다

[mitm_modulation.py](mitm_modulation%201.py)

→ 본인의 절대경로에 맞게 수정!!

```bash
mitmproxy -s /Users/wonchaehee/Desktop/mitm_modulation.py
```

## 로그가 뜨지 않는다면?

flows 하단에 본다면 실행되고 있는 포트가 보일 것이다

지금부터 하단에 보이는 포트를 8080 라고 가정하고 안내하겠다

현재 8080포트에서 flows가 뜨는데, mitm은 다른 포트를 보고 있는 듯하다

아래 명령어를 넣어 8080으로 포트를 바꾸어 주자

host 0.0.0.0 은 모든 ip의 mitm 추적을 허용하는것이니, 그대로 두자

```bash
mitmproxy --certs mitmproxyCA.pem.key.pem --listen-host 0.0.0.0 -p 9999
```

또는

```bash
sudo mitmproxy --certs mitmproxyCA.pem.key.pem --listen-host 0.0.0.0 -p 443
```

## 1. Firefox에서 프록시 설정하기

1. Firefox 실행
2. 주소창에 입력

```bash
about:preferences
```

1. 아래로 스크롤 → 네트워크 설정(Network Settings) → 우측 아래의 설정 클릭
2. 수동 프록시 설정
    1. HTTP 프록시 : (내 컴퓨터 IP)
    2. 포트 8080(또는 본인이 설정한 포트)

1. mitmproxy CA 인증서 등록
2. mitmproxy 실행 후, Firefox 브라우저 접속

```bash
http://mitm.it
```

os 에 맞는 인증서 다운로드

⚠️만약 ”If you see this screen, mitm proxy is not working” 이라면 mitm이 제대로 실행되고 있지 않다

⚠️Client TLS handshake failed. The client does not trust the proxy's certificate

→ 인증서를 클라이언트측이 제대로 신뢰하고 있지 못한 경우

→  Firefox 보안 설정

1. 주소창에 `about:config` 입력
2. 경고 문구 "위험을 감수하고 계속하기" 클릭
3. 아래 키워드 검색:
    
    ```
    security.enterprise_roots.enabled
    ```
    
4. 값이 `false`면 → **더블 클릭해서 `true`로 변경**

---

해당 메뉴얼을 따라했는데

메뉴얼에 나와있지 않은 에러나 지식은

주인장(원채희)보다는 GPT가 알 확률이 높다

물어는 봐도 되지만…🤔

내가…알까?

---

이미지&pdf 텍스트 추출

1. 설치

```bash
pip install easyocr
pip install pymupdf easyocr pillow
```

[mitm_modulation_easyocr_pdf.py](mitm_modulation_easyocr_pdf.py)

1. 실행 명령어(window기준)

```bash
mitmdump -s (mitm_modulation_easyocr_pdf.py경로) --set console_eventlog_verbosity=debug
```