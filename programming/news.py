import requests
import os
from dotenv import load_dotenv

# .env 파일에서 환경변수 로드
load_dotenv()
NEWS_API_KEY = os.getenv("NEWSAPI_API_KEY")

# 뉴스 API로부터 기사 가져오기
def get_news_from_api():
    url = "https://newsapi.org/v2/everything"
    params = {
        'apiKey': NEWS_API_KEY,
        'language': 'ko',        # 한국어 뉴스만 가져오기
        'sortBy': 'publishedAt', # 최신순 정렬
        'pageSize': 30,          # 최대 30개 기사 가져오기
        'q': '뉴스'              # 키워드: 뉴스
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("뉴스 API 오류:", response.text)
        return []
    return response.json().get('articles', [])
