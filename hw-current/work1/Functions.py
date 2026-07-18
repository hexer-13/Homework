from Class import *
from datetime import date

# Вивести відомості про працівників, у яких зарплата вища за середню і вік менше 30-ти років.

def average_salary(input_list):
    average = 0
    try:
        for item in input_list:
            average += item.salary
    except Exception as e:
        print(e)
    if len(input_list) > 0:
        return average / len(input_list)


def salary_more_than_x(input_list,x):
    res_list = []
    try:
        for item in input_list:
            if item.salary > x:
                res_list.append(item)
    except Exception as e:
        print(e)
    if res_list != []:
        return res_list


def older_than_x(input_list,x):
    res_list = []
    try:
        for item in input_list:
            if (2026 - item.date_of_birth.year) > x:
                res_list.append(item)
    except Exception as e:
        print(e)
    if res_list != []:
        return res_list


def print_2(input_list):
    iter_list = iter(input_list)
    try:
        for item in iter_list:
            print(item)
    except StopIteration:
        pass
    except Exception as e:
        print(e)
