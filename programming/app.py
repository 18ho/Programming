from flask import Flask, render_template
from datetime import datetime
import asyncio
from news import get_news_from_api
from summarizer import async_summarize_all

# Flask 앱 생성
app = Flask(__name__)

# 메인 페이지 라우팅
@app.route("/")
def index():
    # 뉴스 API로부터 기사 목록 가져오기
    news_list = get_news_from_api()

    titles = []
    urls = []
    contents = []

    # 각 뉴스 기사에서 제목, URL, 내용을 분리
    for news in news_list:
        title = news.get('title', '')
        desc = news.get('description', '')
        content = news.get('content', '')
        full_text = f"{desc}. {content}"

        titles.append(title)
        urls.append(news.get('url'))
        contents.append(full_text)

    # 비동기로 모든 뉴스 요약 처리
    summaries = asyncio.run(async_summarize_all(contents))

    # 뉴스 제목, 요약, URL을 하나의 리스트로 정리
    summarized_news = []
    for title, summary, url in zip(titles, summaries, urls):
        summarized_news.append({
            'title': title,
            'summary': summary if isinstance(summary, str) else "(요약 실패)",
            'url': url
        })

    # 오늘 날짜 포맷팅
    today = datetime.today().strftime("%Y년 %m월 %d일 %A")

    # 템플릿 렌더링 (index.html)
    return render_template("index.html", news_list=summarized_news, now=today)

# 서버 실행
if __name__ == "__main__":
    app.run(debug=True)
