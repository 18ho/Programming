import requests  # HTTP 요청 모듈
import os        # 환경변수 접근 모듈
from dotenv import load_dotenv  # 환경변수 로딩 모듈

# 환경변수 로딩 (.env 파일 내 API 키)
load_dotenv()
NEWS_API_KEY = os.getenv("NEWSAPI_API_KEY")

def get_news_from_api():
    url = "https://newsapi.org/v2/everything"
    params = {
        'apiKey': NEWS_API_KEY,   # API 인증키
        'language': 'ko',         # 한국어 뉴스만 필터링
        'sortBy': 'publishedAt',  # 최신순 정렬
        'pageSize': 30,           # 기사 최대 30개
        'q': '속보 OR 경제 OR 정치 OR 사회 OR 문화 OR 스포츠 OR IT'  # 명확한 주요 키워드로 뉴스 검색
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("뉴스 API 오류:", response.text)
        return []

    return response.json().get('articles', [])
