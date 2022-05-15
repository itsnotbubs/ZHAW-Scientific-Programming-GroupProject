import imp
import pandas as pd
import yfinance as yf
import matplotlib as plt

tickers = ["SPY", "^TNX"]

data = yf.download(tickers, start="2000-01-01", end = "2022-01-01", period="1d")
print(data)



