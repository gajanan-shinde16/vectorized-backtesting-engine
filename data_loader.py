import yfinance as yf


def fetch_data():

    ticker = "AAPL"
    start_date = "2020-01-01"
    end_date = "2024-01-01"

    print("Downloading market data...")

    df = yf.download(ticker, start=start_date, end=end_date)

    df.to_csv("data/stock_data.csv")

    print("Saved data to data/stock_data.csv")


if __name__ == "__main__":
    fetch_data()