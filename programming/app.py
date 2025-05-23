# Flask 웹 애플리케이션의 메인 실행 파일
from flask import Flask, render_template  # Flask 웹 프레임워크 및 템플릿 렌더링 기능
from datetime import datetime             # 날짜와 시간 처리 모듈
import asyncio                            # 비동기 처리 모듈
from news import get_news_from_api        # 뉴스 데이터 가져오는 모듈
from summarizer import async_summarize_all # 요약 기능 모듈
from dotenv import load_dotenv            # 환경변수 로드용 모듈

# 환경변수(.env 파일) 로딩
load_dotenv()

# Flask 애플리케이션 초기화
app = Flask(__name__)

# 메인 페이지("/") 라우팅
@app.route("/")
def index():
    # 뉴스 API에서 최신 뉴스 데이터 가져오기
    news_list = get_news_from_api()

    # 뉴스 데이터를 분리하여 저장할 리스트 초기화
    titles, urls, contents = [], [], []

    # 뉴스 목록을 순회하며 필요한 정보 추출
    for news in news_list:
        title = news.get('title', '')  # 뉴스 제목
        desc = news.get('description', '')  # 뉴스 설명
        content = news.get('content', '')  # 뉴스 본문
        full_text = f"{desc} {content}"  # 설명과 본문 결합

        # 각 데이터를 리스트에 추가
        titles.append(title)
        urls.append(news.get('url'))
        contents.append(full_text)

    # 뉴스 내용을 비동기적으로 요약하여 리스트로 반환
    summaries = asyncio.run(async_summarize_all(contents))

    # 제목, 요약, URL을 결합하여 최종 뉴스 데이터 구성
    summarized_news = [{
        'title': title,
        'summary': summary if isinstance(summary, str) else "(요약 실패)",
        'url': url
    } for title, summary, url in zip(titles, summaries, urls)]

    # 오늘 날짜를 보기 좋게 포맷팅
    today = datetime.today().strftime("%Y년 %m월 %d일 %A")

    # index.html 템플릿 렌더링 및 데이터 전달
    return render_template("index.html", news_list=summarized_news, now=today)

# Flask 애플리케이션 실행
if __name__ == "__main__":
    app.run(debug=True)
