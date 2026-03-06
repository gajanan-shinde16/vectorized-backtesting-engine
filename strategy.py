import pandas as pd

def moving_average_strategy(data):

    signals = pd.DataFrame(index=data.index)

    signals["price"] = data["Close"]

    signals["short_ma"] = data["Close"].rolling(window=20).mean()
    signals["long_ma"] = data["Close"].rolling(window=50).mean()

    signals["signal"] = 0

    signals.loc[signals["short_ma"] > signals["long_ma"], "signal"] = 1

    signals["positions"] = signals["signal"].diff()

    return signals