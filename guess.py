import os
from dotenv import load_dotenv
import google.generativeai as genai

# .env 파일에 저장된 변수들을 불러옵니다.
load_dotenv()

# 환경 변수에서 키를 가져와 설정합니다.
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

# 2. 분석 함수 정의
def analyze_market_event(target_date, hypothesis):
    prompt = f"""
    당신은 데이터 중심의 퀀트 리서처입니다.
    대상 날짜: {target_date}
    사용자 가설: {hypothesis}
    
    위 날짜에 S&P 500 지수가 급변한 실제 경제적 배경을 분석해주세요.
    사용자의 가설이 맞는지 확인하고, 만약 다른 결정적인 요인(금리 결정, 고용 지표, 특정 기업 실적 등)이 있다면 함께 설명해주세요.
    결과는 퀀트 보고서 형식으로 간결하게 요약하세요.
    """
    
    response = model.generate_content(prompt)
    return response.text

# 3. 팩트 체크 실행
date_to_check = "2025년 4월 9일"
my_guess = "트럼프의 관세 관련 발언으로 인한 시장 변동성 확대"

result = analyze_market_event(date_to_check, my_guess)
print(f"--- {date_to_check} 시장 분석 결과 ---")
print(result)