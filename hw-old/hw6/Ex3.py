rang = list(map(int, input("Введіть перше та останье значення проміжку через пробіл: ").split()))
start = rang[0]
end = rang[1]
my_list = list(range(start, end + 1))

for i in range(start, end+1):
    if i == 1:
        my_list.remove(i)
    for j in range(2, i):
        if i % j == 0 and i in my_list:
            my_list.remove(i)
        else:
            pass

print(my_list)

print("Оберіть наступну операцію \n - 1 - Сумма "
            "простих чисел \n - 2 - Добуток простих чисел")
operation = int(input(" - "))
if operation == 1:
    sum = sum(my_list)
    print("Ваш результат =",sum)
elif operation == 2:
    dob = 1
    for num in my_list:
        dob *= num
    print("Ваш результат =",dob)
else:
    print("Не вірний інпут(")