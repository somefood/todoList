## todoList
todo 게시판 만들기

## git
git clone https://github.com/somefood/todoList.git
master 브랜치 건들지 말고, 브랜치 생성해서 작업하시오.

git checkout -b 브랜치명(design? 일케?)

## 장고 실행
일단 파이썬 설치. (가상환경까진 어려우니 설치만)
> pip install django

로 장고 설치해주고 clone한 디렉토리로 들어가 다음과 같이 입력 `python manage.py runserver`

이후 127.0.0.1:8000으로 접속 가능함

## 프론트 쪽 파일
** 장고 간단히 알아야 할 것들**
1. 정적 파일들을 갖고오기 위해 작업할 html 파일 맨 위에 `{% load static %}`을 입력해주기.
2. 파일 불러올 때 주소를 다음과 같이 한다. ex) `<link rel="stylesheet" href="{% static 'css/styles.css' %}">`

**레이아웃 파일**
templates/_base.html (레이아웃 용, 공통된 틀은 여기서 건들기)

templates/registration (로그인, 회원가입, 회원가입 완료 페이지)

todolist/templates/todolist/index.html (todo list 메인 페이지)

**정적 파일들**
static/css
static/js
