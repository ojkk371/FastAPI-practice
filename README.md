# FastAPI practice

### Project Structure
```bash
.
├── app
│   ├── common
│   │   ├── config.py
│   │   └── consts.py
│   ├── database
│   │   ├── conn.py	# db session 관리 -> 싱글턴 패턴
│   │   └── schema.py
│   ├── middleware
│   │   └── trusted_hosts.py # 기존 starlette 모듈에 except_path 인자 재정의, aws 대비
│   ├── routes
│   │   ├── auth.py
│   │   └── index.py
│   ├── utils
│   │   └── logger.py
│   ├── models.py
│   └── main.py
├── LICENSE
├── README.md
└── setup.py
```

## TODO
#### Install
```bash
git clone https://github.com/ojkk371/FastAPI-practice.git
python3 -m pip install -e .
```

#### 1. 회원가입
- 회원가입
- 비밀번호 해시
- DB 저장
- JWT 생성
- ID/PW 제거하고 QR-생체인증 대체


#### 2. 로그인
- 이메일로 로그인
- QR코드로 로그인
- 터치ID/페이스ID로 로그인

#### 3. 로그인 유저 확인하는 미들웨어 생성
#### 4. 에러 처리
#### 5. 로깅
#### 6. API 키 생성
- 생성
- 폐기
- 재발급

#### 7. ...
