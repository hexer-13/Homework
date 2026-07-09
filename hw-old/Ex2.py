# Найменування
# Кількість
# Ціна
# Виробник
# Дата_випуску
#
# Визначити середню вартість товарів і товар мінімальною вартістю.
import datetime

class Product:
    def __init__(self,name,quantity,price,manufacturer,date_of_manufacture):
        self.__name = name
        self.__quantity = quantity
        self.__price = price
        self.__manufacturer = manufacturer
        self.__date_of_manufacture = date_of_manufacture

    @property
    def name(self):
        return self.__name

    @property
    def quantity(self):
        return self.__quantity

    @property
    def price(self):
        return self.__price

    @property
    def manufacturer(self):
        return self.__manufacturer

    @property
    def date_of_manufacture(self):
        return self.__date_of_manufacture

    def __str__(self):
        return f"|Name:{self.__name}|Quantity: {self.__quantity}|Price: {self.__price}|Manufacturer: {self.__manufacturer}|Date: {self.__date_of_manufacture}|"

item1 = Product("Name1",23,6000,"Guy1", datetime.date(1,1,1))
item2 = Product("Name2",34,4000,"Guy2", datetime.date(2,2,2))
item3 = Product("Name3",45,2000,"Guy3", datetime.date(3,3,3))
item4 = Product("Name4",56,1000,"Guy4", datetime.date(4,4,4))
item5 = Product("Name5",67,3000,"Guy5", datetime.date(5,5,5))
item6 = Product("Name6",78,5000,"Guy6", datetime.date(6,6,6))

items_list = [item1,item2,item3,item4,item5,item6]

def find_average_price(list):
    res = 0
    try:
        for i in list:
            res += i.price
        res /= len(list)
        return res

    except TypeError:
        return "Wrong Input"

    except Exception as e:
        return e


def min_price(in_list):
    res = None
    try:
        for item in in_list:
            if res is None or item.price < res.price:
                res = item
        return res
    except TypeError:
        return "Wrong Input"
    except Exception as e:
        return e


def print2(input_list):
    try:
        gen = (item for item in input_list)
        for i in input_list: print(next(gen))
    except TypeError:
        print("Wrong Input")


print(find_average_price(items_list))
print(min_price(items_list))
print("")
print2(items_list)