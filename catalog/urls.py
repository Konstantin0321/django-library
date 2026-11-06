# catalog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Адрес будет выглядеть как /catalog/book/
    path('book/', views.book_detail, name='book_detail'),
]