a = float(input("Введіть a : "))
b = float(input("Введіть b : "))
c = float(input("Введіть c : "))
D = (b ** 2) - (4 * a * c)
if D < 0:
    x1 = (-b - (D ** 0.5)) / (2 * a)
    x2 = (-b + (D ** 0.5)) / (2 * a)
    print("x1 = ", x1)
    print("x2 = ", x2)
elif D == 0:
    x = (-b - (D ** 0.5)) / (2 * a)
    print("x = ", x)
else:
    print("Дійсних коренів немає")
