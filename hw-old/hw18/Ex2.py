# Завдання: Облік співробітників компанії (складне)!
# Створіть програму на Python для роботи зі співробітниками компанії.
# Умови:
# Створіть базовий клас Employee (Співробітник), який має:
# приватні поля:
# ім'я (__name)
# зарплата (__salary)
# стаж роботи (__years)
# методи:
# отримання даних (get-методи)
# зміни зарплати (set-метод із перевіркою, що зарплата > 0)
# Створіть похідний клас Manager (Менеджер), який успадковує клас Employee та має додаткове поле:
# відділ (department)
# Реалізуйте метод у базовому або похідному класі:
# increase_salary(), який:
# якщо стаж ≥ 10 років → підвищує зарплату на 20%
# якщо стаж ≥ 5 років → підвищує зарплату на 10%
# якщо стаж < 5 років → зарплата не змінюється
# Створіть список співробітників (мінімум 6–8 об'єктів різних типів).
# Розділіть співробітників на три окремі масиви:
# Перший масив — співробітники зі стажем ≥ 10 років (підвищення 20%)
# Другий масив — співробітники зі стажем ≥ 5 років (підвищення 10%)
# Третій масив — співробітники зі стажем < 5 років (без підвищення)
# Для кожного співробітника:
# викличте метод підвищення зарплати
# додайте його у відповідний масив
# Виведіть:
# усі три масиви окремо
# для кожного співробітника: ім'я, стаж, нову зарплату
# Додатково
# Обробіть помилки через try/except (наприклад, неправильний ввід зарплати)
# Додайте метод __str__() для гарного виводу інформації про співробітника
from unittest import case


class Employee:
    def __init__(self,name,salary,years):
        self.__name = name
        self.__salary = salary
        self.__years = years

    @property
    def name(self):
        return self.__name

    @property
    def salary(self):
        return self.__salary

    @property
    def years(self):
        return self.__years

    @name.setter
    def name(self,value):
        try:
            if type(value) is not str:
                raise TypeError("Name must be an string")
            self.__name = value
        except Exception as e:
            print(e)

    @salary.setter
    def salary(self,value):
        try :
            if type(value) is not int or type(value) is not float:
                raise TypeError("Salary must be an integer")
            if value <= 0:
                raise ValueError("Salary cannot be negative")
            self.__salary = value
        except Exception as e:
            print(e)

    @years.setter
    def years(self,value):
        try:
            if type(value) is not int or type(value) is not float:
                raise TypeError("Years must be a number")
            if value < 0:
                raise ValueError("Years cannot be negative")
            self.__years = value
        except Exception as e:
            print(e)


    def increase_salary_exp(self):
        try:
            match self.years:
                case v if v < 5:
                    pass
                case v if 5 <= v < 10:
                    self.__salary += self.salary * 0.1
                case v if v >= 10:
                    self.__salary -= self.salary * 0.2
        except Exception as e:
            print(e)

    def __str__(self):
        return f"| Name: {self.__name} | Salary: {self.__salary} | Years: {self.__years} |"


class Manager(Employee):
    def __init__(self,name,salary,years,department):
        Employee.__init__(self,name,salary,years)
        self.__department = department

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, value):
        try:
            if type(value) is not str:
                raise TypeError("Department must be an string")
            self.__department = value
        except Exception as e:
            print(e)

Guy1 = Employee("Name1", 1000, 1)
Guy2 = Employee("Name2", 2000, 4)
Guy3 = Employee("Name3", 3000, 9)
Guy4 = Employee("Name4", 4000, 14)
Guy5 = Manager("Name5", 1000, 2,"Dep1")
Guy6 = Manager("Name6", 2000, 5,"Dep2")
Guy7 = Manager("Name7", 3000, 10,"Dep3")
Guy8 = Manager("Name8", 4000, 15,"Dep4")

employee_list = [Guy1,Guy2,Guy3,Guy4,Guy5,Guy6,Guy7,Guy8]
less_then_5_list = []
in_between_list = []
more_than_10_list = []


def sort_by_years(in_list):
    try:
        for employee in in_list:
            match employee.years:
                case v if v < 5:
                    less_then_5_list.append(str(employee))
                case v if 5 <= v < 10:
                    employee.increase_salary_exp()
                    in_between_list.append(str(employee))
                case v if v >= 10:
                    employee.increase_salary_exp()
                    more_than_10_list.append(str(employee))
    except Exception as e:
        print(e)

sort_by_years(employee_list)
print(less_then_5_list)
print(in_between_list)
print(more_than_10_list)
