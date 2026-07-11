from Class import *

def ram_more_than(input_list, number):
    res = 0
    res_list = [res]
    try:
        for item in input_list:
            if item.ram > number:
                res_list.append(str(item))
                res += 1
                res_list.pop(0)
                res_list.insert(0,res)
        if res == 0:
            return "No computers with that much RAM"
        else:
            return res_list
    except Exception as e:
        return e

def print_info(input_list):
    if type(input_list) != list:
        print(input_list)
        return None
    iter_list = iter(input_list)
    try:
        while True:
            print(next(iter_list))
    except StopIteration:
        pass

def save_info(input_list):
    with open("Save.py", "w") as f:
        f.write(str(input_list))

def load_info():
    with open("Save.py", "r") as f:
        return f.read()
