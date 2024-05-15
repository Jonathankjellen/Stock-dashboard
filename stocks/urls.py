from django.urls import path
from . import views
from .views import stock_history

urlpatterns = [
    path('', views.stock_list, name='stock_list'),
    path('<str:symbol>/', stock_history, name='stock_history'),
]