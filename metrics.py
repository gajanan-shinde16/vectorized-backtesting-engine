import numpy as np


def performance_metrics(portfolio):

    returns = portfolio["returns"].dropna()

    sharpe = np.sqrt(252) * returns.mean() / returns.std()

    volatility = returns.std() * np.sqrt(252)

    drawdown = (portfolio["total"].cummax() - portfolio["total"]).max()

    print("\nPerformance Summary")
    print("-------------------")
    print("Sharpe Ratio:", round(sharpe, 2))
    print("Volatility:", round(volatility, 2))
    print("Max Drawdown:", round(drawdown, 2))