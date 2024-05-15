from django.shortcuts import render
from django.db.models import Max
from .models import Stock

def stock_list(request):
    latest_stocks = Stock.objects.values('symbol').annotate(latest_date=Max('date'))
    stocks = [Stock.objects.get(symbol=stock['symbol'], date=stock['latest_date']) for stock in latest_stocks]
    
    return render(request, 'stocks/stock_list.html', {'stocks': stocks})

def stock_history(request, symbol):
    stock_history = Stock.objects.filter(symbol=symbol).order_by('-date')
    return render(request, 'stocks/stock_history.html', {'stock_history': stock_history, 'symbol': symbol})
