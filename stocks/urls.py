from django.urls import path
from . import views
from .views import stock_list

urlpatterns = [
    path('', stock_list, name='stock_list'),
]