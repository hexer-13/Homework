import datetime

class Product:
    def __init__(self, seller, name, amount, price, date):
        self.__seller = seller
        self.__name = name
        self.__amount = amount
        self.__price = price
        self.__date = date

    @property
    def seller(self):
        return self.__seller

    @property
    def name(self):
        return self.__name

    @property
    def amount(self):
        return self.__amount

    @property
    def price(self):
        return self.__price

    @property
    def date(self):
        return self.__date


    def __str__(self):
        return f"{self.name}, {self.amount}, {self.price}, {self.date}"


Product1 = Product("Іванов", "Knife", 10,100, datetime.date(2026, 6, 25))
Product2 = Product("Seller2", "Boiler", 2,200, datetime.date(2026, 1, 25))
Product3 = Product("Іванов", "Pan", 3,300, datetime.date(2001, 6, 25))
Product4 = Product("Seller4", "Rope", 4,400, datetime.date(2026, 6, 7))
Product5 = Product("Seller5", "Bag", 5,500, datetime.date(2026, 1, 1))

products = [Product1, Product2, Product3, Product4, Product5]

def count_product_amount_by_sellers(products_in,seller_in):
    count = 0
    res_list = []
    max_cost = 0
    for product in products_in:
        if product.seller == seller_in:
            count += product.amount
            res_list.append(str(product))
            if product.price > max_cost:
                max_cost = product.price
        elif product == products_in[-1] and res_list == []:
            return "Нема продавця з таким іменем"
    print(f"Seller: {seller_in}, quantity of products: {count}, max cost: {max_cost}, products info: {res_list}")
    return count, res_list, max_cost

res = count_product_amount_by_sellers(products,"Іванов")
print(res)