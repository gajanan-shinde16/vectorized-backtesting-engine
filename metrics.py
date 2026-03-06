import numpy as np

def performance_metrics(portfolio):

    returns = portfolio["returns"].dropna()

    sharpe_ratio = np.sqrt(252) * returns.mean() / returns.std()

    volatility = returns.std() * np.sqrt(252)

    max_drawdown = (portfolio["total"].cummax() - portfolio["total"]).max()

    print("Sharpe Ratio:", round(sharpe_ratio, 2))
    print("Volatility:", round(volatility, 2))
    print("Max Drawdown:", round(max_drawdown, 2))