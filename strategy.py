import pandas as pd


def moving_average_strategy(price_data):

    df = pd.DataFrame(index=price_data.index)

    df["price"] = price_data["Close"]

    # simple moving averages
    df["ma_short"] = price_data["Close"].rolling(20).mean()
    df["ma_long"] = price_data["Close"].rolling(50).mean()

    # trading signal
    df["signal"] = 0

    df.loc[df["ma_short"] > df["ma_long"], "signal"] = 1

    # detect signal changes
    df["trade"] = df["signal"].diff()

    return df