# catalog/urls.py
from django.urls import path
from . import dogs, views

urlpatterns = [
    path('dogs/', dogs.dog_gallery, name='dog_gallery'),
    # Адрес будет выглядеть как /catalog/book/
    path('book/', views.book_detail, name='book_detail'),
]