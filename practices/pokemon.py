import re
from functools import lru_cache

from .api import ApiError, get_json


POKEMON_URL = "https://pokeapi.co/api/v2/pokemon/"


@lru_cache(maxsize=128)
def pokemon_details(name):
    name = name.strip().lower()
    if not re.fullmatch(r"[a-z][a-z0-9-]*", name):
        raise ApiError("Введите имя покемона латиницей, например clefairy.")

    data = get_json(f"{POKEMON_URL}{name}/")
    return {
        "name": data["name"],
        "types": [item["type"]["name"] for item in data["types"]],
        "weight": data["weight"] / 10,
        "height": data["height"] / 10,
        "abilities": [item["ability"]["name"] for item in data["abilities"]],
        "stats": {item["stat"]["name"]: item["base_stat"] for item in data["stats"]},
    }


def print_details(pokemon):
    print(f"Имя: {pokemon['name']}")
    print(f"Тип: {', '.join(pokemon['types'])}")
    print(f"Вес: {pokemon['weight']:g} кг")
    print(f"Рост: {pokemon['height']:g} м")
    print(f"Способности: {', '.join(pokemon['abilities'])}")


def main():
    try:
        data = get_json(f"{POKEMON_URL}?limit=20&offset=0")
        for index, pokemon in enumerate(data["results"], start=1):
            print(f"{index}. {pokemon['name']}")

        name = input("Имя покемона: ")
        print_details(pokemon_details(name))
    except ApiError as error:
        print(error)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
