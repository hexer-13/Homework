# бренд (brand), розмір екрану (screen size), ціна (price), об'єм оперативної пам'яті (RAM).

class Laptop:
    def __init__(self, brand, screen_size, price, ram):
        self.__brand = self.__validate_brand(brand)
        self.__screen_size = self.__validate_screen_size(screen_size)
        self.__price = self.__validate_price(price)
        self.__ram = self.__validate_ram(ram)


    @property
    def brand(self):
        return self.__brand
    @property
    def screen_size(self):
        return self.__screen_size
    @property
    def price(self):
        return self.__price
    @property
    def ram(self):
        return self.__ram


    def __validate_brand(self, value):
        if not isinstance(value, str):
            raise TypeError("Brand must be a string")
        return value

    def __validate_screen_size(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise TypeError("Screen size must be a number")
        return value

    def __validate_price(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise TypeError("Ram must be a number")
        return value

    def __validate_ram(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise TypeError("RAM must be a number")
        return value


    @brand.setter
    def brand(self, value):
        self.__brand = self.__validate_brand(value)

    @screen_size.setter
    def screen_size(self, value):
        self.__screen_size = self.__validate_screen_size(value)

    @price.setter
    def price(self, value):
        self.__price = self.__validate_price(value)

    @ram.setter
    def ram(self, value):
        self.__ram = self.__validate_ram(value)


    def __str__(self):
        return f"|{self.__brand}|{self.__screen_size}|{self.__price}|{self.__ram}|"