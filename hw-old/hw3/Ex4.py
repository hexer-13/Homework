import math
print("Доступні операції :\n\t"
      "1 - Додавання\n\t"
      "2 - Віднімання\n\t"
      "3 - Множення\n\t"
      "4 - Ділення\n\t"
      "5 - Зведення в ступінь\n\t"
      "6 - Квадратний корінь\n\t"
      "7 - Кубічний корінь\n\t"
      "8 - Синус\n\t"
      "9 - Косинус\n\t"
      "10 - Тангенс\n")
op = int(input("Оберіть операцію : "))
match op:
      case int(1):
            a = float(input("Введіть перше число : "))
            b = float(input("Введіть друге число : "))
            print("Сумма ", a , 'i', b , "=", a + b)
      case int(2):
            a = float(input("Введіть перше число : "))
            b = float(input("Введіть друге число : "))
            print("Різниця ", a, 'i', b, "=", a - b)
      case int(3):
            a = float(input("Введіть перше число : "))
            b = float(input("Введіть друге число : "))
            print("Добуток ", a, 'i', b, "=", a * b)
      case int(4):
            a = float(input("Введіть перше число : "))
            b = float(input("Введіть друге число : "))
            print("Частка ", a, 'i', b, "=", a / b)
      case int(5):
            a = float(input("Введіть перше число : "))
            b = float(input("Введіть друге число : "))
            print(a, 'в ступені', b, "=", a ** b)
      case int(6):
            x = float(input("Введіть число : "))
            y = math.sqrt(x)
            print ("Квадратним коренем", x , "є" , y , "та", -y)
      case int(7):
            x = float(input("Введіть число : "))
            y = math.cbrt(x)
            print("Кубічним коренем", x, "є", y)
      case int(8):
            x = float(input("Введіть число : "))
            y = math.sin(x)
            print("Синусом", x, "є", y)
      case int(9):
            x = float(input("Введіть число : "))
            y = math.cos(x)
            print("Косинусом", x, "є", y)
      case int(10):
            x = float(input("Введіть число : "))
            y = math.tan(x)
            print("Тангенсом", x, "є", y)
      case _:
            print("Такої опції немає")