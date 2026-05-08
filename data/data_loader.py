import numpy as np
import pandas as pd
import yfinance as yf
import datetime as dt

# Fetching Data
def fetch_data(ticker,start_date,end_date):
    try:
        data = yf.download(ticker,start=start_date,end=end_date)
        if isinstance(data.columns, pd.MultiIndex):
            # yfinance returns columns like (Price, Ticker) for single-symbol downloads.
            # Keep OHLCV names and remove the redundant ticker level.
            data.columns = data.columns.droplevel("Ticker")
            data.columns.name = None
        return data
    except Exception as e:
        print(f"Error Fetching Data {e}")