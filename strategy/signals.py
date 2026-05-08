import numpy as np
import pandas as pd 

def signal_generator(df):
    df['Signal'] = 0
    df.loc[(df['Z_Score'] < -2) & (df['RSI'] < 30), 'Signal'] = 1
    df.loc[df['RSI'] > 60, 'Signal'] = -1

    return df