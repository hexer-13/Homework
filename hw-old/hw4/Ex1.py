# Дано числа a і b (a < b). Виведіть суму всіх натуральних чисел від a до b (включно).
a = 7
b = 12
res = 0
for i in range(a,b+1):
    res += i
print(res)