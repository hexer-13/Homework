from objects import *

def find_most_storage(input_list):
    res = None
    try:
        for item in input_list:
            if res is None or item.quantity > res.quantity:
                res = item
        return res
    except Exception as e:
        print(e)

def print_2(input_item):
    x = iter(input_item.list_info())
    try:
        while True:
            print(f"|{next(x)}|")
    except StopIteration:
        pass

def save_info(input_item):
    with open("save.py", "w") as f:
        f.write(input_item)

def load_info():
    with open("save.py", "r") as f:
        print(f.read())