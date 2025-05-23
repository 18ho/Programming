import os              # 환경변수 관리 모듈
import asyncio         # 비동기 프로그래밍 모듈
import httpx           # 비동기 HTTP 요청 모듈
from dotenv import load_dotenv  # 환경변수 로딩 모듈

# 환경변수에서 OpenAI API 키 로드
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

# 하나의 뉴스 본문 내용을 비동기로 요약하는 함수
async def async_summarize(content):
    if not content:
        return "(요약할 내용 없음)"

    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {openai_api_key}",
        "Content-Type": "application/json"
    }
    
    # 개선된 요약 프롬프트 (구체적이고 명확한 지침 포함)
    prompt = (
        "당신은 뉴스 콘텐츠를 요약하는 전문가입니다. "
        "다음 뉴스 기사의 핵심 정보를 정확하게 파악한 후, 다음의 규칙에 따라 한국어로 깔끔하게 요약해주세요:\n\n"
        "1. 기사의 핵심 주제를 첫 문장에서 반드시 명시적으로 언급합니다.\n"
        "2. 반드시 핵심적인 인물, 사건, 장소, 시간, 결과 등 핵심정보를 포함합니다.\n"
        "3. 전체 길이는 정확히 3~5문장 내외로 작성합니다.\n"
        "4. 내용이 중간에 끊기거나 의미가 불명확한 부분이 없어야 합니다.\n"
        "5. 읽는 사람이 원문을 읽지 않아도 내용을 명확히 이해할 수 있도록 요약합니다.\n\n"
        f"뉴스 기사 본문:\n{content}"
    )

    payload = {
        "model": "gpt-3.5-turbo", # 사용한 ai모델
        "messages": [{
            "role": "user",
            "content": prompt
        }],
        "temperature": 0.3,  # 낮은 temperature로 명확한 결과 유도
        "max_tokens": 300
    }

    try:
        # OpenAI API를 비동기 방식으로 호출하여 요약 요청
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            result = response.json()
            return result['choices'][0]['message']['content'].strip()
    except Exception as e:
        print("요약 실패:", e)
        return "(요약 실패)"


# 여러 뉴스 본문 내용을 동시에 비동기로 요약하는 함수
async def async_summarize_all(news_list):
    # 비동기 요약 작업 리스트 생성 및 실행
    tasks = [async_summarize(news) for news in news_list]
    return await asyncio.gather(*tasks, return_exceptions=True)
