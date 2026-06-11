int_list = [1,2,3,5,5,7,4,2,1,6,8,95,2,35,8,0,1,2,3,4,5,]
new_list = []
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []
list8 = []
list9 = []
list10 = []
for item in int_list:
    if item % 2 != 0:
        new_list.append(item)
print("int_list:", int_list)
print("new_list:", new_list)
rep = int(input("Введіть кількість копій списку new_list (Максимум 10): "))
if rep > 10:
    print("Забагато копій, буде 10")
for i in range(1, rep+1):
    match i:
        case 1:
            list1 = new_list.copy()
        case 2:
            list2 = new_list.copy()
        case 3:
            list3 = new_list.copy()
        case 4:
            list4 = new_list.copy()
        case 5:
            list5 = new_list.copy()
        case 6:
            list6 = new_list.copy()
        case 7:
            list7 = new_list.copy()
        case 8:
            list8 = new_list.copy()
        case 9:
            list9 = new_list.copy()
        case 10:
            list10 = new_list.copy()

int_list.clear()
print("int_list очищено")