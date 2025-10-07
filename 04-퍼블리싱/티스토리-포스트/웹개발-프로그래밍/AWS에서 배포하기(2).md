# AWS에서 배포하기(2)

> **원본 포스트 ID**: 189
> **발행일**: 2025-06-15 02:41:36
> **카테고리**: project/웹개발

## 📝 원문 내용

**EC2 인스턴스에 컴퓨터에서 원격으로 접속하기**

* * *

<https://filezilla-project.org/>

![](./img/189_img.png)

설치가 안된다면 참고할 사이트

<https://hyejin.tistory.com/537>

[ 파일질라 설치안됨 해결 https://filezilla-project.org/ FileZilla - The free FTP solution Overview Welcome to the homepage of FileZilla®, the free FTP solution. The FileZilla Client not only supports FTP, but also FTP over TLS (FTPS) and SFTP. It is open source software distribut hyejin.tistory.com ](https://hyejin.tistory.com/537)

![](./img/189_img_1.png)

여기에서 제 임대 컴퓨터를 연결해봅시다

![](./img/189_img_2.png)

접속 화면

![](./img/189_img_3.png)

임대컴퓨터에 업로드

![](./img/189_img_4.png)

git bash 에서 명령어로 접속해봅시다.
    
    
    ssh - i 키파일 ubuntu@ip주소

![](./img/189_img_5.png)

접속하면 이런식으로 제가 만든 폴더인 www가 있는걸 확인할수있습니다

**EC2를 Node.js 서버로 세팅하고 리뷰사이트 실행**

* * *
    
    
    curl -sL https://deb.nodesource.com/setup_18.x | sudo -E bash -
    
    sudo apt-get install -y nodejs
    
    sudo apt-get install build-essential
    
    sudo -s //관리자 권한으로 전환
    npm install -g pm2

디 설치가 되면은 서버를 실행시킵니다. 

![](./img/189_img_6.png)

이 상태로는 들어갈수가 없기 때문에 vim 명령어로 app.js의 포트번호를 보고 그 포트번호에 맞춰서 아마존내 임대컴퓨터의 3000번 포트를 열어줘야한다.

![](./img/189_img_7.png)

연결 확인

![](./img/189_img_8.png)

**도메인 구매하기**

* * *

<https://www.gabia.com/>

[ 웹을 넘어 클라우드로. 가비아 그룹웨어부터 멀티클라우드까지 하나의 클라우드 허브 www.gabia.com ](https://www.gabia.com/)

![](./img/189_img_9.png)

**포트번호 80으로 바꿔주기**

* * *

vim app.js 로 열어준다음 포트번호 수정

![](./img/189_img_10.png)

수정하고 저장하고 나갈때는 :wq로 저장합니다.
    
    
    pm2 logs

이 명령어로 pm2가 실행중인지 봅니다 만약 실행중이라면 
    
    
    pm2 delete all
    pm2 start app.js --name app

이제 브라우저에서 확인해봅시다

![](./img/189_img_11.png)

이제 가비아에서 산 도메인을 연결해봅시다.

![](./img/189_img_12.png)

여기서 1차,2차,3차를 다 지워줍니다.

<https://aws.amazon.com/ko/route53/>

[ Amazon Route 53 - DNS 서비스 - AWS Amazon Virtual Private Cloud(VPC)에 사용자 지정 도메인 이름을 할당하고 액세스합니다. DNS 데이터를 퍼블릭 인터넷에 노출하지 않고 내부 AWS 리소스 및 서버를 사용합니다. aws.amazon.com ](https://aws.amazon.com/ko/route53/)

![](./img/189_img_13.png)

여기서 도메인을 설정하면

![](./img/189_img_14.png)

이런식으로 네임서버를 4개정도준다 이걸 가비아에 입력하면 된다.

![](./img/189_img_15.png)

이제 진짜로 도메인을 연결해보는 시간입니다.

![](./img/189_img_16.png)


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
