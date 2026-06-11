def average(a,b,c):
    return (a+b+c)/3

while True:
    print("Введіть 3 числа для обрахунку їх середнього арифметичного"
          "\n(Введення літери чи пустого поля завершить програму)")
    inp_1 = input("Введіть перше число - ")
    if inp_1.isdigit():
        num1 = float(inp_1)
    else:
        print("Виходимо з програми")
        break

    inp_2 = input("Введіть перше число - ")
    if inp_2.isdigit():
        num2 = float(inp_2)
    else:
        print("Виходимо з програми")
        break

    inp_3 = input("Введіть перше число - ")
    if inp_3.isdigit():
        num3 = float(inp_3)
    else:
        print("Виходимо з програми")
        break

    print("Середнє арифметичне заданих значень -", average(num1,num2,num3))