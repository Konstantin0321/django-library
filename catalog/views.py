# catalog/views.py
from django.shortcuts import render


def book_detail(request):
    # 1. Подготавливаем данные (контекст) в виде словаря
    context = {
        'title': 'Мастер и Маргарита',
        'author': 'Михаил Булгаков',
        'year': 1967,
        'description': 'Роман о визите дьявола в Москву 1930-х годов.'
    }

    # 2. Рендерим шаблон и передаем туда контекст
    return render(request, 'catalog/book_detail.html', context)