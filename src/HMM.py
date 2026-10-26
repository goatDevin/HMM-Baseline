import yfinance as yf
import pandas as pd
import numpy as np

dat = yf.Ticker("NVDA")
df = dat.history(period="1y", interval="1d")

df["Log_Returns"] = np.log(df["Close"] / df["Close"].shift(1))

print(df.head())
