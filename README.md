# Django-NovelAssistant

- Django Rest Framework를 이용해 챗봇 API를 제작하는 프로젝트입니다.
- 프론트엔드 리포지토리: [NovelAssistant-FE](https://github.com/bloodsteelrain/NovelAssistant-FE)

## 1. 목표와 기능

### 1.1 목표

- Django Rest Framework를 제작하여 기존 HTML, CSS, JS 프로젝트에 연결시키는 것.

### 1.2 기능

1. 소설 설정 챗봇 기능
   1. 플롯, 등장인물, 에피소드 생성
   2. 질문과 생성된 설정은 데이터베이스에 저장
   3. 생성된 설정이 맘에 들지 않을 시 삭제
2. 로그인/회원가입 기능
   1. 회원가입
   2. 로그인(access token 생성)
   3. 챗봇 이용에 인증 기능 추가
   4. 챗봇 이용 횟수 제한 추가
3. 기타 추가 기능
   1. 회원가입 시 프로필 생성
   2. 프로필 조회 및 수정

## 2. 개발 환경 및 배포 URL

### 2.1 기술 스택

- <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
- <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">
- <img src="https://img.shields.io/badge/sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white">
- <img src="https://img.shields.io/badge/openai-412991?style=for-the-badge&logo=openai&logoColor=white">
- <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
- <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white">
- <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">

### 2.2 개발 환경

- Python==3.11.4
- Django==4.2.3
- django-cors-headers==4.2.0
- djangorestframework==3.14.0
- djangorestframework-simplejwt==5.2.2
- openai==0.27.8
- Pillow==10.0.0

### 2.3 배포 URL

- 백엔드: 미정
- 프론트엔드: [Github pages](https://bloodsteelrain.github.io/NovelAssistant-FE/)

## 3. 프로젝트 구조와 개발 일정

### 3.1 프로젝트 구조

- 백엔드

```
📦 Django-GPTProject-BE
├─ .gitignore
├─ README.md
├─ chat_project
│  ├─ __init__.py
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py
├─ chatbot
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ templates
│  │  └─ chatbot
│  │     └─ base.html
│  ├─ tests.py
│  ├─ throttling.py
│  ├─ urls.py
│  └─ views.py
├─ manage.py
├─ requirements.txt
└─ user
   ├─ __init__.py
   ├─ admin.py
   ├─ apps.py
   ├─ migrations
   │  ├─ 0001_initial.py
   │  ├─ 0002_alter_profile_introduce_alter_profile_nickname.py
   │  └─ __init__.py
   ├─ models.py
   ├─ serializers.py
   ├─ tests.py
   ├─ urls.py
   └─ views.py
```

- 프론트엔드

```
📦 Django-GPTProject-FE
├─ README.md
├─ css
│  ├─ common.css
│  ├─login-join.css
│  └─ style.css
├─ img
│  ├─header_image.jpg
│  ├─loading_image.gif
├─ index.html
├─ join.html
├─ js
│  ├─API.js
│  ├─eraser.js
│  ├─ join.js
│  ├─ loading.js
│  ├─login.js
│  ├─main.js
│  ├─ modal.js
│  ├─ profile.js
│  ├─profile_edit.js
│  ├─scroll.js
│  └─ status.js
├─ login.html
├─ profile.html
└─ profile_edit.html
```

### 3.2 플로우차트

![flowchart](https://github.com/bloodsteelrain/Django-GPTProject-BE/assets/131739343/84204405-9c75-4bfc-ac13-6c6c3fc57127)

### 3.3 데이터베이스 모델

![chatbot-diagram](https://github.com/bloodsteelrain/Django-GPTProject-BE/assets/131739343/59dc747b-4ecf-4bdb-a9f6-dd5e313797fd)

### 3.4 개발 일정

2023.07.26 ~ 2023.08.02

## 4. UI

- 메인 페이지
  ![127 0 0 1_5500_index html](https://github.com/bloodsteelrain/Django-GPTProject-BE/assets/131739343/4fddc676-3ff3-4270-a977-c015dee57728)

- 챗봇 답변 저장 부분
  ![127 0 0 1_5500_index html_저장](https://github.com/bloodsteelrain/Django-GPTProject-BE/assets/131739343/5aa64730-e5df-4a87-8b31-84c30beecebe)

## 5. 기능

1. 비로그인 시 챗봇 사용 불가
   ![비로그인시](https://github.com/bloodsteelrain/Django-GPTProject-BE/assets/131739343/617514c7-8ed4-4b18-a88e-5d7c13899e1c)

2. 회원가입
   ![회원가입](https://github.com/bloodsteelrain/Django-GPTProject-BE/assets/131739343/9c6bec75-7ff1-4cb3-9ff0-ddc529a070a6)

3. 로그인
   ![로그인](https://github.com/bloodsteelrain/Django-GPTProject-BE/assets/131739343/74f1b981-49a6-48f7-a1e6-f7b2d5995cf8)

   ![액세스토큰](https://github.com/bloodsteelrain/NovelAssistant-BE/assets/131739343/9b0b427e-50c5-4c6d-a28c-a24a1f8a37d8)

4. 프로필 보기, 수정
   ![프로필](https://github.com/bloodsteelrain/Django-GPTProject-BE/assets/131739343/207a2735-9d41-4540-aa72-f74a4686ddef)

5. 챗봇 실행
   ![챗봇실행](https://github.com/bloodsteelrain/Django-GPTProject-BE/assets/131739343/cc18b2c0-7158-4645-a236-e18435cf621c)

6. 답변 삭제
   ![삭제하기](https://github.com/bloodsteelrain/Django-GPTProject-BE/assets/131739343/975df31a-032b-4bcd-8577-b7ecc342052a)

7. 횟수 제한(하루 5회)
   ![횟수제한](https://github.com/bloodsteelrain/Django-GPTProject-BE/assets/131739343/ed8dab9b-9e24-4b58-8953-b64bba47004f)

8. 로그아웃
   ![로그아웃](https://github.com/bloodsteelrain/Django-GPTProject-BE/assets/131739343/b9ca05f2-f843-4d15-8fff-59fe7fdab763)

## 6. 느낀점

1. DRF 사용
2. 백 - 프론트 연결
3. JWT를 사용한 토큰 발급, 보안
4. 예상치 못한 에러들

## 7. 보완 목록

1. 챗봇 답변을 게시글로 생성
2. Refresh token 활용
3. 프로필 사진 표시
4. UI
5. 배포
