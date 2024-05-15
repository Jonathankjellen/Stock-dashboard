import yfinance as yf
from django.core.management.base import BaseCommand
from stocks.models import Stock

class Command(BaseCommand):
    help = 'Populate stock data'

    def handle(self, *args, **kwargs):
        stock_symbols = ['AAPL', 'GOOGL', 'MSFT']  # Add your desired stock symbols here
        for symbol in stock_symbols:
            self.stdout.write(f"Fetching data for {symbol}...")
            data = yf.download(symbol, start="2020-01-01", end="2024-01-01")
            for index, row in data.iterrows():
                Stock.objects.update_or_create(
                    symbol=symbol,
                    date=index,
                    defaults={
                        'open_price': row['Open'],
                        'high_price': row['High'],
                        'low_price': row['Low'],
                        'close_price': row['Close'],
                        'volume': row['Volume'],
                    }
                )
            self.stdout.write(f"Data for {symbol} populated.")
