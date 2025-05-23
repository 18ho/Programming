# 프로그래밍 입문

## 4팀

정현호 박건우 김동인 이호영

<br><br><br><br>

# 뉴스 요약 웹 서비스

### VSCode 터미널 열고

### 파이썬 설치돼있는지 확인 (안뜨면 파이썬 설치)

```python
python --version
# 또는
py --version
```

### Python이라는 단어만 뜨고 버전이 표시되지 않으면
```
where python 
```
### 아무것도 안나오면 PATH 문제인듯 (재설치)
https://www.python.org/downloads/
### 설치 시 반드시 "Add Python to PATH" 체크하고 설치

### 설치 확인
```python
python --version
py --version
```

### pip 설치돼있는지 확인

```python
python -m pip --version
# 또는
py -m pip --version
```

### pip이 설치되어 있지 않다면

```python
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
# 또는
py get-pip.py
```

### pip 설치 확인

```python
python -m pip --version
# 또는
py -m pip --version
```

### 필요한 패키지 설치(httpx는 비동기 요청용)

```python
python -m pip install Flask openai requests python-dotenv httpx
# 또는
py -m pip install Flask openai requests python-dotenv httpx
```

### .env 파일 만들기(프로젝트 폴더에)

```python
OPENAI_API_KEY=발급받은_키
NEWSAPI_API_KEY=발급받은_뉴스_API_키
```

Openai Api키 발급(카드 등록 필요)

https://platform.openai.com/api-keys

NewsAPI 키 발급

https://newsapi.org/register

### openai 라이브러리 (위에서 했으면 필요X)

```python
python -m pip install openai
# 또는
py -m pip install openai
```

### 프로젝트 폴더 구조

```python
/프로젝트
├── [app.py]
├── [news.py]
├── [summarizer.py]
├── .env
├── static/ << 폴더임
│   └── style.css
└── templates/ << 폴더임
		├── base.html
		└── index.html
```

### 서버 실행(터미널 열고)

```python
python app.py

py app.py
```

### 브라우저 열고

[http://localhost:5000](http://localhost:5000/)
