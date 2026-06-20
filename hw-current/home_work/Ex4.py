# Створіть клас, який описує автомобіль.
# Створіть клас автосалону, що містить в собі список автомобілів, доступних для продажу, і функцію продажу заданого автомобіля.

class Auto:
    def __init__(self, number, name, brand,color,rundown,price):
        self.number = number
        self.name = name
        self.brand = brand
        self.color = color
        self.rundown = rundown
        self.price = price

    def __str__(self):
        return f'{self.number}, {self.name}, {self.brand}, {self.color}, {self.rundown} - {self.price}$'

    def __repr__(self):
        return f'{self.number}, {self.name}, {self.brand}, {self.color}, {self.rundown} - {self.price}$'


class Dealership:
    def __init__(self,name):
        self.name = name
        self.cars_list = []

    def __str__(self):
        return f'{self.name}'

def sell(dealer):
    print(dealer)
    cars_list = dealer.cars_list
    for car in cars_list:
        print(f"selling {car}")
    while True:
        user_input = input('Enter car ID you wish to buy: ')
        for car in cars_list:
            if user_input == str(car.number):
                print(f"You bought - {car}")
                break


auto1 = Auto(1,"car1","brand1","color1","rundown1","price1")
auto2 = Auto(2,"car2","brand2","color2","rundown2","price2")
auto3 = Auto(3,"car3","brand3","color3","rundown3","price3")
auto4 = Auto(4,"car4","brand4","color4","rundown4","price4")
auto5 = Auto(5,"car5","brand5","color5","rundown5","price5")

dealer1 = Dealership("dealer1")
dealer1.cars_list = [auto1,auto2,auto3,auto4,auto5]

sell(dealer1)