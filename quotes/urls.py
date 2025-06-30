# quotes/urls.py

from django.urls import path
from .views import add_quote, random_quote


urlpatterns = [
    path('add/', add_quote, name='add_quote'),
    path('random/', random_quote, name='random_quote'),  # новый маршрут
]