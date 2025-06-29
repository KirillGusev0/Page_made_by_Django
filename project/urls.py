# project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),           # административка
    path('', include('quotes.urls')),          # маршруты приложения quotes
]