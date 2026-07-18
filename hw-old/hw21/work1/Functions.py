from Objects import *

# Визначити кількість працівників, старших за 60 років, і надрукувати всі відомості про них.

def older_than_x(input_list,x):
    if not isinstance(x, (int, float)) or not isinstance(input_list,list):
        print("Input must be a list and a number")
        return None
    res_list = []
    res = 0
    try:
        for element in input_list:
            if (2026 - element.year_of_birth) > x:
                res+=1
                res_list.append(element)
        if res == 0:
            print ("Результату не знайдено")
            return None
    except Exception as e:
        print(e)
    return [f"Found results: {res}", *res_list]


def print_2(input_list):
    if not isinstance(input_list, list):
        print("Input must be a list")
        return None
    iter_list = iter(input_list)
    try:
        for i in input_list:
            print(next(iter_list))
    except Exception as e:
        print(e)


