# Библиотека и практики по Django

Для запуска нужны Python 3.10+ и интернет для запросов к API. Команды выполняются из корня репозитория.

## Задачи №2 и №3 из лекции

Проект `library` и приложение `catalog` уже настроены. Страница книги с данными из контекста Django доступна по адресу [localhost:8000/catalog/book/](http://localhost:8000/catalog/book/).

## Практика №1. Поиск покемона

```sh
python -m practices.pokemon
```

Программа выводит первые 20 имён из PokéAPI. Введите, например, `clefairy`, чтобы увидеть тип, вес, рост и способности.

## Практика №2. Галерея пород собак

```sh
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Откройте [localhost:8000/catalog/dogs/](http://localhost:8000/catalog/dogs/) и введите `african, chow, dingo`. Для подпород используйте имена из списка, например `hound/afghan`.

## Практика №3. Менеджер команды Pokémon

```sh
python -m practices.pokemon_team
```

Добавьте двух покемонов по имени, например `pikachu` и `clefairy`, и выберите тренировочный бой. Первым атакует покемон с большей скоростью, при равной скорости ходит первый выбранный. Урон равен атаке за вычетом половины защиты с округлением вниз, минимум 1. Команда хранится до выхода из программы. Бой не меняет характеристики участников.

Источники данных: [PokéAPI](https://pokeapi.co/docs/v2), [Dog API](https://dog.ceo/dog-api/documentation/).
