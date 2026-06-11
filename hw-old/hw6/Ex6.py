new_list = [1, 3, 5, 5, 7, 1, 95, 35, 1, 3, 5]
checker = int(input("Введіть число на перевірку: "))
pos = []
if checker in new_list:
    rep = new_list.count(checker)
    print(rep)
    check_list = new_list.copy()
    a = 1
    for item in check_list:
        if item == checker:
            pos.append(check_list.index(item)+1)
            a = check_list.index(item)
            check_list.pop(a)
            check_list.insert(a,())
    print("Кількість повторів та позиції",checker, "у списку:", rep,"-", pos)
else:
    print(checker, "нема у списку")