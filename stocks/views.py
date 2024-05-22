from django.shortcuts import render
from django.db.models import Max, F
from .models import Stock
import json
from datetime import datetime,timedelta
def stock_list(request):
    latest_stocks = Stock.objects.values('symbol').annotate(latest_date=Max('date'),close_price=Max('close_price'))
    stocks = [{
        'symbol': entry['symbol'],
        'date': entry['latest_date'].strftime('%Y-%m-%d'),
        'close': float(entry['close_price']),
    } for entry in latest_stocks]

    top_stocks = sorted(stocks, key=lambda x: x['close'], reverse=True)[:5]

    return render(request, 'stocks/stock_list.html', {'stocks': stocks,'top_stocks':top_stocks})

def stock_history(request, symbol):
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=5*365)
    stock_history = Stock.objects.filter(symbol=symbol, date__range=(start_date, end_date)).order_by('date')

    # stock_history = Stock.objects.filter(symbol=symbol).order_by('-date')
    stock_data = [{
        'date': entry.date.strftime('%Y-%m-%d'),
        'open': float(entry.open_price),
        'high': float(entry.high_price),
        'low': float(entry.low_price),
        'close': float(entry.close_price),
        'volume': entry.volume,
    } for entry in stock_history]

    return render(request, 'stocks/stock_history.html', {'stock_history': stock_data, 'symbol': symbol})
