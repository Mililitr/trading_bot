import yfinance as yf

class YFinanceDataFetcher:
    def get_data(self, symbol, interval, period):
        data = yf.download(tickers=symbol, interval=interval, period=period)
        return data