import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

print("Everything works!")

stock = yf.Ticker("AAPL")
data = stock.history(period="5d")

print(data[["Close"]])