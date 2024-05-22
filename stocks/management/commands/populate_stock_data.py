import yfinance as yf
from django.core.management.base import BaseCommand
from stocks.models import Stock
from datetime import datetime,timedelta
class Command(BaseCommand):
    help = 'Populate stock data'

    def handle(self, *args, **kwargs):
        stock_symbols = ['AAPL', 'GOOGL', 'MSFT','ABB.ST','ERICb.ST','INVEb.ST','TELIA.ST','EVO.ST','ERIC-B.ST']  # Add your desired stock symbols here
        today = datetime.now().date()
        end_date = today - timedelta(days=1)

        start_date = end_date - timedelta(days=5*365)

        for symbol in stock_symbols:
            latest_date = Stock.objects.filter(symbol=symbol).order_by('-date').first()
            if latest_date:
                latest_date = latest_date.date
            else:
                latest_date = start_date
            if latest_date < end_date:
                self.stdout.write(f"Fetching data for {symbol} from {latest_date} to {end_date}")
                history = yf.download(symbol, start=latest_date, end=end_date)
                for date, row in history.iterrows():
                    stock, created = Stock.objects.update_or_create(
                        symbol=symbol,
                        date=date,
                        defaults={
                            'open_price': row['Open'],
                            'high_price': row['High'],
                            'low_price': row['Low'],
                            'close_price': row['Close'],
                            'volume': row['Volume'],
                        }
                    )
                    if created:
                            self.stdout.write(f'Added data for {symbol} on {date}')
                    else:
                        self.stdout.write(f'Updated data for {symbol} on {date}')
        self.stdout.write(self.style.SUCCESS('Successfully updated the database with the latest stock data'))

