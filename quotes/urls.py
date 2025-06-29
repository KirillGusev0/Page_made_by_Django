# quotes/urls.py

from django.urls import path
from .views import add_quote 

urlpatterns = [
    path('add/', add_quote, name='add_quote'),  
]