import yfinance as yf

def download_data():

    data = yf.download(
        "AAPL",
        start="2020-01-01",
        end="2024-01-01"
    )

    data.to_csv("data/stock_data.csv")

    print("Data downloaded")

if __name__ == "__main__":
    download_data()