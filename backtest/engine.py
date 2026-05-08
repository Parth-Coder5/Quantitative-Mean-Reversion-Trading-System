import numpy as np
import pandas as pd

def run_backtest(df):
    capital = 100000
    cash = capital
    position = 0
    entry_price = 0

    for i in range(len(df)):
        row = df.iloc[i]
        price = row['Close']
        signal = row['Signal']

        if signal == 1 and position == 0:
            invest_amount = 0.4*cash
            shares = invest_amount / price    
            
            position = shares
            entry_price = price
            cash -= invest_amount

            print(f"BUY @ {price} | shares: {shares}")
        
        elif signal == -1 and position > 0:
            sell_value = position * price
            profit = (price - entry_price) * position

            cash += sell_value
            print(f"SELL @ {price} | P&L: {profit:.2f} | cash: {cash:.2f}")

            position = 0
            entry_price = 0
        elif position > 0 and price <= 0.97*entry_price:
            sell_value = position * price
            profit = (price - entry_price) * position

            cash += sell_value
            print(f"STOP LOSS HIT @ {price}")

            position = 0
            entry_price = 0


        # mark-to-market (agar open position bachi ho)
    final_value = cash + (position * df.iloc[-1]['Close'])

    print("----- RESULT -----")
    print(f"Final Value: {final_value:.2f}")
    print(f"Total Profit: {final_value - capital:.2f}")        