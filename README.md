# Vectorized Trading Strategy Backtesting Engine

Small Python project for testing trading strategies on historical stock data.

The project downloads market data, generates trading signals using a moving average crossover strategy, and evaluates performance.

## Features

- Moving average trading strategy
- Portfolio simulation
- Sharpe ratio, volatility, drawdown metrics
- Buy/sell signal visualization

## Tech Stack

Python  
Pandas  
NumPy  
Matplotlib  

## Run

Install dependencies:

pip install -r requirements.txt

Download market data:

python data_loader.py

Run backtest:

python backtest.py