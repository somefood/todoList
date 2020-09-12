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

이후 브라우저에서 127.0.0.1:8000으로 접속 가능함

## 프론트 쪽 파일
** 장고 간단히 알아야 할 것들**
1. 정적 파일들을 갖고오기 위해 작업할 html 파일 맨 위에 `{% load static %}`을 입력해주기.
2. 파일 불러올 때 주소를 다음과 같이 한다. ex) `<link rel="stylesheet" href="{% static 'css/styles.css' %}">`
3. 다른 html최상단 파일을 보면 `{% extends '_base.html' %}` 있는데, _base.html 내용을 불러와서 사용하겠다는 의미이다. 공통 틀로 사용할 파일을 상속받아 사용하는 것이다.
4. _base.html과 다른 파일을 보면 `{% block content %}{% endblock %}` 같은게 있는데, 블락이라 부르고 이것을 통해서 공통틀을 사용하면서 내용을 가꿀 수 있는 것이다.
예로, 내가 body안에다가 블락을 넣었는데, _base.html을 상속받은 login.html은 똑같은 이름의 블락을 정의해주면 된다. 그리고 그 블락안에 내용을 넣으면 body안에 내용들이 들어갈 것이다.
블락을 씀으로 공통된 내용들을 굳이 다시 작성할 필요도 없고 해당 파일에 들어갈 내용만 작성하면 되니 이득이다.


**레이아웃 파일**
templates/_base.html (레이아웃 용, 공통된 틀은 여기서 건들기)

templates/registration (로그인, 회원가입, 회원가입 완료 페이지)

todolist/templates/todolist/index.html (todo list 메인 페이지)

**정적 파일들**
static/css
static/js
