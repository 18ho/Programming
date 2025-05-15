import os
import asyncio
import httpx
from dotenv import load_dotenv

# .env 파일에서 환경변수 로드
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

# 하나의 뉴스 본문을 요약하는 비동기 함수
async def async_summarize(content):
    if not content:
        return "(요약할 내용 없음)"
    
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {openai_api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": f"다음 내용을 3~5문장으로 자연스럽고 완결성 있게 요약해줘. 문장이 중간에 끊기지 않게 해줘:\n{content}"
            }
        ],
        "temperature": 0.7,
        "max_tokens": 300
    }

    try:
        # httpx 비동기 클라이언트로 OpenAI API 호출
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            result = response.json()
            return result['choices'][0]['message']['content'].strip()
    except Exception as e:
        print("요약 실패:", e)
        return "(요약 실패)"

# 여러 뉴스 기사들을 동시에 요약하는 함수
async def async_summarize_all(news_list):
    tasks = [async_summarize(news) for news in news_list]
    return await asyncio.gather(*tasks, return_exceptions=True)
