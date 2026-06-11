my_list = []
my_elements = int(input("Введіть кількість елементів вашого цілочисельного списку: "))
for i in range(1, my_elements+1):
    my_list.append(int(input("Введіть наступне число вашого списку: ")))
print("Ваш список:", my_list)
print("Та має довжину:", len(my_list))
print("Меню:\n"
      "- 1 - Вивести список у зворотному порядку\n"
      "- 2 - Вивести список за зростанням\n")
op = int(input("Натисніть клавішу бажаної операції та Enter: "))
if op == 1:
    reversed_list = list(reversed(my_list))
    print(reversed_list)
elif op == 2:
    sorted_list = sorted(my_list)
    print(sorted_list)