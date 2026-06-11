from unittest import case

libra = {"a":"na","b":"bo"}
task = 0


while task != 4:
    print("Список операцій:"
          "\n 1 - Знайти твір"
          "\n 2 - Ввести зміни"
          "\n 3 - Перелік творів"
          "\n 4 - Вийти з бібліотеки")
    print()
    task = int(input("Введіть номер бажаної операції:"))
    match task:
        case 1:
            print()
            task = input("Введіть ім'я автора, чию інформацію переглянути").lower()
            print(task,"-",libra.get(task))
            print()
        case 2:
            task = int(input("Введіть номер бажаної операції:"))
            match task:
                case 1:

                case 2:
                    pass
                case 3:
                    pass
        case 3:
            task = int(input("Введіть номер бажаної операції:"))
            match task:
                case 1:
                    pass
                case 2:
                    pass
        case 4:
            pass
        case _:
            print("WAAD")