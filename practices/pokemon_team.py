from .api import ApiError
from .pokemon import pokemon_details, print_details


def print_profile(pokemon):
    print_details(pokemon)
    stats = ", ".join(f"{name}: {value}" for name, value in pokemon["stats"].items())
    print(f"Характеристики: {stats}")


def training_battle(first, second):
    fighters = [first, second]
    fighters.sort(key=lambda pokemon: pokemon["stats"]["speed"], reverse=True)
    if fighters[0]["stats"]["speed"] == fighters[1]["stats"]["speed"]:
        print("При равной скорости первым ходит первый выбранный покемон.")

    hp = {pokemon["name"]: pokemon["stats"]["hp"] for pokemon in fighters}
    attacker, defender = fighters
    while True:
        damage = max(1, attacker["stats"]["attack"] - defender["stats"]["defense"] // 2)
        hp[defender["name"]] = max(0, hp[defender["name"]] - damage)
        remaining = hp[defender["name"]]
        print(f"{attacker['name']} наносит {damage} урона. У {defender['name']} осталось {remaining} HP.")
        if remaining == 0:
            print(f"Победитель: {attacker['name']}")
            return
        attacker, defender = defender, attacker


def main():
    team = {}
    while True:
        print("\n1. Добавить\n2. Удалить\n3. Показать команду\n"
              "4. Найти по имени\n5. Тренировочный бой\n0. Выйти")
        try:
            choice = input("Действие: ").strip()
            if choice == "0":
                return
            if choice == "1":
                name = input("Кого добавить? ").strip().lower()
                pokemon = pokemon_details(name)
                if pokemon["name"] in team:
                    print("Этот покемон уже в команде.")
                else:
                    team[pokemon["name"]] = pokemon
                    print(f"{pokemon['name']} добавлен в команду.")
            elif choice == "2":
                name = input("Кого удалить? ").strip().lower()
                if team.pop(name, None) is None:
                    print("Этого покемона нет в команде.")
                else:
                    print(f"{name} удалён из команды.")
            elif choice == "3":
                if not team:
                    print("Команда пуста.")
                for pokemon in team.values():
                    print_profile(pokemon)
                    print()
            elif choice == "4":
                name = input("Кого найти? ").strip().lower()
                print_profile(team.get(name) or pokemon_details(name))
            elif choice == "5":
                if len(team) < 2:
                    print("Добавьте в команду двух покемонов.")
                    continue
                first = input("Первый покемон: ").strip().lower()
                second = input("Второй покемон: ").strip().lower()
                if first == second or first not in team or second not in team:
                    print("Выберите двух разных покемонов из команды.")
                else:
                    training_battle(team[first], team[second])
            else:
                print("Выберите пункт от 0 до 5.")
        except ApiError as error:
            print(error)
        except (EOFError, KeyboardInterrupt):
            print()
            return


if __name__ == "__main__":
    main()
