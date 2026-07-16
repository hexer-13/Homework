class Product:
    def __init__(self, name, quantity, price, year, manufacturer):
        self.__name = name
        self.__quantity = quantity
        self.__price = price
        self.__year = year
        self.__manufacturer = manufacturer

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
    def year(self):
        return self.__year
    @property
    def manufacturer(self):
        return self.__manufacturer

    @name.setter
    def name(self, name):
        self.__name = name
    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity
    @price.setter
    def price(self, price):
        self.__price = price
    @year.setter
    def year(self, year):
        self.__year = year
    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer

    def __str__(self):
        return f"{self.__name},{self.__quantity},{self.__price},{self.__year},{self.__manufacturer}"

    def list_info(self):
        return [self.__name, self.__quantity, self.__price, self.__year, self.__manufacturer]