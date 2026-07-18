from Objects import *

# Вивести відомості про машини марки «Toyota», зареєстровані до 2007-го року.

def car_of_brand_registered_before(input_list,input_brand,year):
    res_list = []
    try:
        for item in input_list:
            if item.brand == input_brand and item.date_of_registration.year < year:
                res_list.append(item)
    except Exception as e:
        print(e)
        return None
    return res_list

def print_2(input_list):
    iter_list = iter(input_list)
    try:
        while True:
            print(next(iter_list))
    except StopIteration:
        return None
    except Exception as e:
        print(e)