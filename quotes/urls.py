# quotes/urls.py

from django.urls import path
from .views import add_quote, random_quote, like_quote, dislike_quote, top_quotes, quote_detail

urlpatterns = [
    path("add/", add_quote, name="add_quote"),
    path("random/", random_quote, name="random_quote"),
    path("like/<int:quote_id>/", like_quote, name="like_quote"),
    path("dislike/<int:quote_id>/", dislike_quote, name="dislike_quote"),
    path("top/", top_quotes, name="top_quotes"),
    path("quote/<int:quote_id>/", quote_detail, name="quote_detail"), 
]
