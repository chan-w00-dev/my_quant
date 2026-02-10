import yfinance as yf
import streamlit as st

# 1. 제목 작성
st.title("Chanwoo의 퀀트 첫걸음")

# 2. 데이터 불러오기 (미국 주가 지수 S&P 500)
ticker = '^GSPC'
data = yf.download(ticker, start="2024-01-01")

# 3. 화면에 출력
st.subheader("S&P 500 최근 데이터")
st.write(data.tail())

# 4. 간단한 차트
st.line_chart(data['Close'])