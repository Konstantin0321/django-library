from django.contrib import admin  # ← ЭТОЙ СТРОКИ НЕ ХВАТАЕТ!
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Добро пожаловать в библиотеку!</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('', home, name='home'),
]