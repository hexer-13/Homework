list1 = list(map(int, input("Введіть перший список через пробіл: ").split()))
list2 = list(map(int, input("Введіть другий список через пробіл: ").split()))
print(list1)
print(list2)
res_list = list1 + list2
for item in res_list:
    if item in list1 and item in list2:
        res_list.remove(item)
    else:
        pass

print(res_list)
sorted_list = sorted(res_list)
print(sorted_list)
print(sorted_list[::-1])