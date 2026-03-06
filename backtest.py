import pandas as pd
import matplotlib.pyplot as plt

from strategy import moving_average_strategy
from metrics import performance_metrics


def run_backtest():

    # Load CSV (first column is date index)
    data = pd.read_csv(
        "data/stock_data.csv",
        index_col=0,
        parse_dates=[0]
    )

    # Ensure Close is numeric
    data["Close"] = pd.to_numeric(data["Close"], errors="coerce")

    # Drop bad rows
    data = data.dropna()

    # Generate signals
    signals = moving_average_strategy(data)

    initial_capital = 10000

    positions = pd.DataFrame(index=signals.index)
    positions["shares"] = 100 * signals["signal"]

    portfolio = pd.DataFrame(index=signals.index)

    portfolio["holdings"] = positions["shares"] * data["Close"]

    pos_diff = positions.diff()

    portfolio["cash"] = initial_capital - (
        pos_diff["shares"] * data["Close"]
    ).cumsum()

    portfolio["total"] = portfolio["cash"] + portfolio["holdings"]

    portfolio["returns"] = portfolio["total"].pct_change()

    # Print performance
    performance_metrics(portfolio)

    # Plot results
    portfolio["total"].plot(title="Portfolio Value")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value")
    plt.show()



if __name__ == "__main__":
    run_backtest()