import pandas as pd
import matplotlib.pyplot as plt

from strategy import moving_average_strategy
from metrics import performance_metrics


def run_backtest():

    # load historical price data
    data = pd.read_csv(
        "data/stock_data.csv",
        index_col=0,
        parse_dates=[0]
    )

    # ensure numeric values
    data["Close"] = pd.to_numeric(data["Close"], errors="coerce")
    data = data.dropna()

    # generate strategy signals
    signals = moving_average_strategy(data)

    initial_capital = 10000

    positions = pd.DataFrame(index=signals.index)
    positions["shares"] = 100 * signals["signal"]

    portfolio = pd.DataFrame(index=signals.index)

    # value of held shares
    portfolio["holdings"] = positions["shares"] * data["Close"]

    trades = positions.diff()

    # remaining cash after trades
    portfolio["cash"] = initial_capital - (
        trades["shares"] * data["Close"]
    ).cumsum()

    portfolio["total"] = portfolio["cash"] + portfolio["holdings"]

    portfolio["returns"] = portfolio["total"].pct_change()

    # buy and hold benchmark
    shares = initial_capital / data["Close"].iloc[0]
    portfolio["buy_hold"] = shares * data["Close"]

    # print performance metrics
    performance_metrics(portfolio)

    # generate charts
    plot_results(data, signals, portfolio)


def plot_results(data, signals, portfolio):

    plt.figure(figsize=(12,6))

    plt.plot(data.index, data["Close"], label="Price")

    # buy signals
    buy = signals[signals["trade"] == 1]
    plt.scatter(
        buy.index,
        buy["price"],
        marker="^",
        color="green",
        label="Buy"
    )

    # sell signals
    sell = signals[signals["trade"] == -1]
    plt.scatter(
        sell.index,
        sell["price"],
        marker="v",
        color="red",
        label="Sell"
    )

    plt.title("Moving Average Strategy Signals")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()

    plt.show()

    # portfolio comparison chart
    plt.figure(figsize=(12,6))

    plt.plot(
        portfolio.index,
        portfolio["total"],
        label="Strategy"
    )

    plt.plot(
        portfolio.index,
        portfolio["buy_hold"],
        label="Buy & Hold"
    )

    plt.title("Strategy vs Buy & Hold")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value")

    plt.legend()

    plt.show()


if __name__ == "__main__":
    run_backtest()