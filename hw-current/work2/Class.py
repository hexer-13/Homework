# Марка автомобіля
# Виробник
# Тип
# Рік випуску
# Дата реєстрації
from datetime import date


class Car:
    def __init__(self ,brand ,manufacturer ,type ,year_of_manufacture ,date_of_registration):
        self.__brand = self.__validate_brand(brand)
        self.__manufacturer = self.__validate_manufacturer(manufacturer)
        self.__type = self.__validate_type(type)
        self.__year_of_manufacture = self.__validate_year_of_manufacture(year_of_manufacture)
        self.__date_of_registration = self.__validate_date_of_registration(date_of_registration)


    @property
    def brand(self):
        return self.__brand
    @property
    def manufacturer(self):
        return self.__manufacturer
    @property
    def type(self):
        return self.__type
    @property
    def year_of_manufacture(self):
        return self.__year_of_manufacture
    @property
    def date_of_registration(self):
        return self.__date_of_registration

    @brand.setter
    def brand(self,value):
        self.__brand = self.__validate_brand(value)

    @manufacturer.setter
    def manufacturer(self,value):
        self.__manufacturer = self.__validate_manufacturer(value)

    @type.setter
    def type(self,value):
        self.__type = self.__validate_type(value)

    @year_of_manufacture.setter
    def year_of_manufacture(self,value):
        self.__year_of_manufacture = self.__validate_year_of_manufacture(value)

    @date_of_registration.setter
    def date_of_registration(self,value):
        self.__date_of_registration = self.__validate_date_of_registration(value)

    def __validate_brand(self,value):
        if not isinstance(value,str):
            raise TypeError('Brand must be a string')
        return value

    def __validate_manufacturer(self,value):
        if not isinstance(value,str):
            raise TypeError('Manufacturer must be a string')
        return value

    def __validate_type(self,value):
        if not isinstance(value,str):
            raise TypeError('Type must be a string')
        return value

    def __validate_year_of_manufacture(self,value):
        if not isinstance(value,(int,float)):
            raise TypeError('Year of Manufacture must be a number')
        return value

    def __validate_date_of_registration(self,value):
        if not isinstance(value,date):
            raise TypeError('Date of Registration must be a date')
        return value

    def __str__(self):
        return f"|{self.__brand} |{self.__manufacturer} |{self.__type} |{self.__year_of_manufacture} |{self.__date_of_registration}"