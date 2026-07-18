# Назва
# Кількостей
# Ціна
# Рік виготовлення
# Виробник
# Визначити найдорожчий товар на складі та надрукувати всі відомості про нього.

class Product:
    def __init__(self,name,quantity,price,year,manufacturer):
        self.__name = self.__validate_name(name)
        self.__quantity = self.__validate_quantity(quantity)
        self.__price = self.__validate_price(price)
        self.__year = self.__validate_year(year)
        self.__manufacturer = self.__validate_manufacturer(manufacturer)

    def __validate_name(self,value):
        if not isinstance(value,str):
            raise ValueError("Name must be a string")
        return value

    def __validate_quantity(self,value):
        if not isinstance(value,(int,float)) or value < 0:
            raise ValueError("Quantity must be a number, 0 or above")
        return value

    def __validate_price(self,value):
        if not isinstance(value,(int,float)):
            raise ValueError("Price must be a number")
        return value

    def __validate_year(self,value):
        if not isinstance(value,(int,float)) and value > 2026:
            raise ValueError("Year must be a number")
        return value

    def __validate_manufacturer(self,value):
        if not isinstance(value,str):
            raise ValueError("Manufacturer must be a string")
        return value

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
    def name(self,value):
        self.__validate_name(value)
        self.__name = value
    @quantity.setter
    def quantity(self,value):
        self.__validate_quantity(value)
        self.__quantity = value
    @price.setter
    def price(self,value):
        self.__validate_price(value)
        self.__price = value
    @year.setter
    def year(self,value):
        self.__validate_year(value)
        self.__year = value
    @manufacturer.setter
    def manufacturer(self,value):
        self.__validate_manufacturer(value)
        self.__manufacturer = value

    def __str__(self):
        return f"|{self.__name}||{self.__quantity}||{self.__price}||{self.__year}||{self.__manufacturer}|"