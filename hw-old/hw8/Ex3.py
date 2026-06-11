def add(a,b):
    return a+b
def subtract(a,b): return a-b
def multiply(a,b): return a*b
def divide(a,b):
    if b == 0:
        print("Ділення на нуль не можливе, бро")
        return None
    else:
        return a/b
def power(a,b): return a**b
def square_root(a): return a ** 0.5
def cube_root(a): return a ** 1/3


option = None
while option != 8:
    print("Меню операцій:"
          "\n 1 - Додавання"
          "\n 2 - Віднімання"
          "\n 3 - Множення"
          "\n 4 - Ділення"
          "\n 5 - Піднесення до степеня"
          "\n 6 - Квадратний корінь"
          "\n 7 - Кубічний корінь"
          "\n 8 - Вихід"
          "\n")
    option = input("Введіть номер бажаної операції (1-8): ")
    print()
    match option:
        case "1":
            num1 = float(input("Введіть перший доданок: "))
            num2 = float(input("Введіть другий доданок: "))
            print(num1,"додати",num2,"=",add(num1,num2))
        case "2":
            num1 = float(input("Введіть зменшуване: "))
            num2 = float(input("Введіть від’ємник: "))
            print(num1, "мінус", num2, "=", subtract(num1, num2))
        case "3":
            num1 = float(input("Введіть перший множник: "))
            num2 = float(input("Введіть другий множник: "))
            print(num1, "помножити на", num2, "=", multiply(num1, num2))
        case "4":
            num1 = float(input("Введіть ділене: "))
            num2 = float(input("Введіть дільник: "))
            if divide(num1, num2) == None:
                pass
            else:
                print(num1, "поділити на", num2, "=", divide(num1, num2))
        case "5":
            num1 = float(input("Введіть число: "))
            num2 = float(input("Введіть степінь: "))
            print(num1, "у степені", num2, "=", power(num1, num2))
        case "6":
            num = float(input("Введіть ваше число: "))
            print("Квадратний корінь",num, "=", square_root(num))
        case "7":
            num = float(input("Введіть ваше число: "))
            print("Кубічний корінь", num, "=", cube_root(num))
        case "8":
            print("Вихід успішний!")
            break
        case _:
            print("Помилка введення")
    input("Натисніть Enter щоб продовжити: ")