### 1. 디렉토리 구조
```bash
WATCHMATE
├── user_app
│   ├── api
│   │    ├── serializers.py
│   │    ├── urls.py
│   │    └── views.py
│   └── models.py
├── watchlist_app
│   ├── api
│   │    ├── permissions.py
│   │    ├── Serializers.py
│   │    ├── urls.py
│   │    └── views.py
│   └── model.py
├── watchmate
│    ├── settings.py
│    └── urls.py
└── manage.py
``` 

### 1. watchmate: default app
- settings.py: Django 프레임워크의 모든 개발 환경 세팅
- urls.py: urlpatterns를 구현

### 2. watchlist_app: 주요 항목에 대한 기능 구현 및 항목 클래스 간 연결 app
- api: api구현하는 부분을 api폴더를 만들어 해당 폴더 내에서 필요한 부분들을 구현 
    - permissions.py: Admin유저 혹은 직접 리뷰를 남긴 유저가 아니면 READ밖에 할 수 없도록 하는 기능 구현
    - Serializers.py: 모델에서 데이터를 뽑아 응답으로 보낼 때, 그 데이터의 형태를 정해주는 serializer들을 구현
    - urls.py: watchlist_app의 기능들을 토대로 동작하는 urlpatterns를 구현. 리뷰에 대한 나열, 생성, 자세한 내용 보기 등의 기능 존재
    - views.py: watchlist_app의 기능들에 대한 응답 구현
- models.py: watchlist_app의 기능들 구현

### 3. user_app: User Authentication에 대한 app
- api: api구현하는 부분을 api폴더를 만들어 해당 폴더 내에서 필요한 부분들을 구현 
    - serializers.py: Register에 대한 serializer구현
    - urls.py: register, login, logout, token을 확인하고 refresh 하는 urlpattern들을 구현
    - views.py: logout, Register에 대한 응답 구현
- models.py: auth token을 생성하는 기능 구현
