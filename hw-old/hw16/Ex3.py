# Найменування
# Кількість
# Ціна
# Виробник
# Дата_надходження_на_склад
# Вивести відомості про товари з ціною вищою за середню.
import datetime

class Product:
    def __init__(self,name, quantity, cost, seller, date):
        self.__name = name
        self.__quantity = quantity
        self.__cost = cost
        self.__seller = seller
        self.__date = date

    @property
    def name(self):
        return self.__name

    @property
    def quantity(self):
        return self.__quantity

    @property
    def cost(self):
        return self.__cost

    @property
    def seller(self):
        return self.__seller

    @property
    def date(self):
        return self.__date

    def __str__(self):
        return f"{self.name} {self.quantity} {self.cost} {self.seller} {self.date}"

Product1 = Product("Name1",1,100,"Seller1",datetime.date(2026,1,1))
Product2 = Product("Name2",2,200,"Seller2",datetime.date(2026,2,2))
Product3 = Product("Name3",3,300,"Seller3",datetime.date(2026,3,3))
Product4 = Product("Name4",4,400,"Seller4",datetime.date(2026,4,4))
Product5 = Product("Name5",5,500,"Seller5",datetime.date(2026,5,5))

products = [Product1,Product2,Product3,Product4,Product5]

def info_for_above_average_price(products):
    all_cost = 0
    res_list = []
    for product in products:
        all_cost += product.cost
    average_price = all_cost/len(products)
    for product in products:
        if product.cost > average_price:
            res_list.append(str(product))
    if len(res_list) > 0:
        return res_list
    else:
        return "None"

print(info_for_above_average_price(products))