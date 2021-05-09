import pandas as pd
import yfinance as yf


tickers = ["DLR","REGN","EFX","CNC","BLL","SBAC","DG","AMT","EA","VRTX","VRSN","VFC","GDX"]

data = yf.download(tickers=tickers, period='3y', interval='1d')
data.to_csv("data_2y_before_3_month.csv")
