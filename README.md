# Quantitative Mean Reversion Trading System

A quantitative trading strategy built using Python for detecting mean reversion opportunities in NSE stocks using statistical indicators and backtesting techniques.

---

## Features

- Z-Score based signal generation
- RSI filtering logic
- Stop-loss risk management
- Portfolio allocation logic
- Multi-stock backtesting engine
- Historical NSE stock analysis

---

## Indicators Used

- Moving Average (MA20)
- Standard Deviation (STD20)
- Z-Score
- Relative Strength Index (RSI)
- Volume Moving Average

---

## Strategy Logic

### Buy Signal
- Z-Score < -2
- RSI < 30

### Sell Signal
- Z-Score >= 0
- RSI > 60

### Risk Management
- 10% Stop Loss
- Capital allocation per stock

---

## Tech Stack

- Python
- Pandas
- NumPy
- yFinance
- Jupyter Notebook

---

## Project Structure

```bash
backtest/
data/
strategy/
README.md
requirements.txt
app.ipynb
```

---

## Future Improvements

- Machine Learning probability model
- Live market integration
- Streamlit dashboard
- Advanced portfolio optimization

---

## Author

Kavyansh Mishra  
Aspiring Quantitative Developer & AI Engineer
