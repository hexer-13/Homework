from Class_apple import *

def biggest_screen(input_list):
    if not isinstance(input_list, (list,tuple,set)):
        raise TypeError("Input must be a list, tuple or set")
    res = None
    try:
        for i in input_list:
            if res == None or i.screen_size > res.screen_size:
                res = i
        return res
    except Exception as e:
        print(e)


def smallest_screen(input_list):
    if not isinstance(input_list, (list,tuple,set)):
        raise TypeError("Input must be a list, tuple or set")
    res = None
    try:
        for i in input_list:
            if res == None or i.screen_size < res.screen_size:
                res = i
        return res
    except Exception as e:
        print(e)


def cheapest_laptop(input_list):
    if not isinstance(input_list, (list,tuple,set)):
        raise TypeError("Input must be a list, tuple or set")
    res = None
    try:
        for i in input_list:
            if res == None or i.price < res.price:
                res = i
        return res
    except Exception as e:
        print(e)


def most_expensive_laptop(input_list):
    if not isinstance(input_list, (list,tuple,set)):
        raise TypeError("Input must be a list, tuple or set")
    res = None
    try:
        for i in input_list:
            if res == None or i.price > res.price:
                res = i
        return res
    except Exception as e:
        print(e)


def most_ram(input_list):
    if not isinstance(input_list, (list,tuple,set)):
        raise TypeError("Input must be a list, tuple or set")
    res = None
    try:
        for i in input_list:
            if res == None or i.ram > res.ram:
                res = i
        return res
    except Exception as e:
        print(e)


def least_ram(input_list):
    if not isinstance(input_list, (list,tuple,set)):
        raise TypeError("Input must be a list, tuple or set")
    res = None
    try:
        for i in input_list:
            if res == None or i.ram < res.ram:
                res = i
        return res
    except Exception as e:
        print(e)


def save_info(item):
    with open("save","r") as file:
        print(f"Saved as line {len(file.readlines()) + 1}")
    with open("save","a") as file:
        file.write(str(item))
        file.write("\n")

def read_info(line_x):
    with open("save","r") as file:
        lines = file.readlines()
        res = lines[line_x-1].strip()
        res = str(res)
    return res


def listify_info(item_laptop):
    item_str = str(item_laptop)
    item_str = item_str[1:len(item_str)-1]
    info_list = item_str.split('|')
    return info_list

def print_info(item_x):
    if not isinstance(item_x,(Laptop, Apple, str)):
        raise TypeError("Input must be a Laptop, Apple, or list")
    try:
        iter_list = iter(listify_info(item_x))
        while True:
            print(f"|{next(iter_list)}")
    except Exception as e:
        print(e)