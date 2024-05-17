from django.shortcuts import render
from django.db.models import Max
from .models import Stock
import json
def stock_list(request):
    latest_stocks = Stock.objects.values('symbol').annotate(latest_date=Max('date'))
    stocks = [Stock.objects.get(symbol=stock['symbol'], date=stock['latest_date']) for stock in latest_stocks]
    
    return render(request, 'stocks/stock_list.html', {'stocks': stocks})

def stock_history(request, symbol):
    stock_history = Stock.objects.filter(symbol=symbol).order_by('-date')
    stock_data = [{
        'date': entry.date.strftime('%Y-%m-%d'),
        'open': float(entry.open_price),
        'high': float(entry.high_price),
        'low': float(entry.low_price),
        'close': float(entry.close_price),
        'volume': entry.volume,
    } for entry in stock_history]

    return render(request, 'stocks/stock_history.html', {'stock_history': stock_data, 'symbol': symbol})
