# Прізвище
# Ім'я
# По батькові
# Посада
# Зарплата
# Дата народження
# Вивести відомості про працівників, у яких зарплата вища за середню і вік менше 30-ти років.
from datetime import date


class Worker:
    def __init__(self,surname,name,middle_name,position,salary,date_of_birth):
        self.__surname = self.__validate_surname(surname)
        self.__name = self.__validate_name(name)
        self.__middle_name = self.__validate_middle_name(middle_name)
        self.__position = self.__validate_position(position)
        self.__salary = self.__validate_salary(salary)
        self.__date_of_birth = self.__validate_date_of_birth(date_of_birth)

    def __validate_surname(self, value):
        if not isinstance(value, str):
            raise ValueError("Surname must be a string")
        return value

    def __validate_name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        return value

    def __validate_middle_name(self, value):
        if not isinstance(value, str):
            raise ValueError("Middle name must be a string")
        return value

    def __validate_position(self, value):
        if not isinstance(value, str):
            raise ValueError("Position must be an string")
        return value

    def __validate_salary(self, value):
        if not isinstance(value, (int,float)):
            raise ValueError("Salary must be a number")
        return value

    def __validate_date_of_birth(self, value):
        if not isinstance(value, date):
            raise ValueError("Date must be a date")
        return value

    @property
    def surname(self):
        return self.__surname
    @property
    def name(self):
        return self.__name
    @property
    def middle_name(self):
        return self.__middle_name
    @property
    def position(self):
        return self.__position
    @property
    def salary(self):
        return self.__salary
    @property
    def date_of_birth(self):
        return self.__date_of_birth

    @surname.setter
    def surname(self,value):
        self.__surname = self.__validate_surname(value)
    @name.setter
    def name(self,value):
        self.__name = self.__validate_name(value)
    @middle_name.setter
    def middle_name(self,value):
        self.__middle_name = self.__validate_middle_name(value)
    @position.setter
    def position(self,value):
        self.__position = self.__validate_position(value)
    @salary.setter
    def salary(self,value):
        self.__salary = self.__validate_salary(value)
    @date_of_birth.setter
    def date_of_birth(self,value):
        self.__date_of_birth = self.__validate_date_of_birth(value)

    def __str__(self):
        return f"|{self.__surname} |{self.__name} |{self.__middle_name} |{self.position} |{self.salary} |{self.__date_of_birth}|"