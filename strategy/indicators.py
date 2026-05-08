import numpy as np
import pandas as pd

def calculate_rsi(df, window=14):
    delta = df.diff()

    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.ewm(alpha=1/window, min_periods=window, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1/window, min_periods=window, adjust=False).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi


def add_indicators(df):
    df['MA20'] = df['Close'].rolling(window=20).mean()
    df['STD20'] = df['Close'].rolling(window=20).std()
    df['Z_Score'] = (df['Close'] - df['MA20']) / df['STD20']
    df['VOL_MA20'] = df['Volume'].rolling(window=20).mean()
    df['MA50'] = df['Close'].rolling(window=50).mean()
    df['prev_close'] = df['Close'].shift(1)

    return df