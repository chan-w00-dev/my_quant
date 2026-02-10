# %% [1] 데이터 가져오기
import pandas as pd
import yfinance as yf

# S&P 500 데이터 (최근 10년)
df = yf.download("^GSPC", period="10y")

# %% [2] 일일 변동률 계산하기
# (오늘 종가 - 어제 종가) / 어제 종가
df['Daily_Return'] = df['Close'].pct_change()

# %% [3] 변동성(절댓값)이 가장 컸던 'TOP 5' 날짜 뽑기
# abs()는 절댓값을 구하는 함수입니다 (폭락도 변동성이니까요!)
top5_volatility = df['Daily_Return'].abs().sort_values(ascending=False).head(5)

print("--- 지난 10년간 가장 변동성이 컸던 5일 ---")
print(top5_volatility)
# %%
