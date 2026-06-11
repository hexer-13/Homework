import math
x = float(input("Введіть число x, для котрого дійсне -𝜋 <= x <= 𝜋 : "))
if -math.pi <= x <= math.pi:
    x = x * 3
    y = math.cos(x)
    print("Результат:", round(y,4))
else:
    print("Не правильний x")