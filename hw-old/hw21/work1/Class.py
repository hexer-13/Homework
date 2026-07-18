# Прізвище
# Рік народження
# Посада
# Зарплата
# Освіта
# Визначити кількість працівників, старших за 60 років, і надрукувати всі відомості про них.

class Worker:
    def __init__(self, surname, year_of_birth, position, salary, education):
        self.__surname = self.__validate_surname(surname)
        self.__year_of_birth = self.__validate_year_of_birth(year_of_birth)
        self.__position = self.__validate_position(position)
        self.__salary = self.__validate_salary(salary)
        self.__education = self.__validate_education(education)

    def __validate_surname(self,value):
        if not isinstance(value, str) or len(value) < 2:
            raise ValueError("Некоректне прізвище")
        return value

    def __validate_year_of_birth(self,value):
        if not isinstance(value, int) or value > 2026:
            raise ValueError("Вік не повинен бути від'ємним")
        return value

    def __validate_position(self,value):
        if not isinstance(value, str) or len(value) < 2:
            raise ValueError("Некоректна посада")
        return value

    def __validate_salary(self,value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Зарплата не може бути від'ємною")
        return value

    def __validate_education(self,value):
        if not isinstance(value, str) or len(value) < 2:
            raise ValueError("Некоректна освіта")
        return value

    @property
    def surname(self):
        return self.__surname
    @property
    def year_of_birth(self):
        return self.__year_of_birth
    @property
    def position(self):
        return self.__position
    @property
    def salary(self):
        return self.__salary
    @property
    def education(self):
        return self.__education

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @year_of_birth.setter
    def year_of_birth(self, year_of_birth):
        self.__year_of_birth = year_of_birth

    @position.setter
    def position(self, position):
        self.__position = position

    @salary.setter
    def salary(self, salary):
        self.__salary = salary

    @education.setter
    def education(self, education):
        self.__education = education

    def __str__(self):
        return f"|Surname:{self.__surname}|Year of birth:{self.year_of_birth}|Position:{self.__position}|Salary:{self.salary}|Education:{self.education}|"

