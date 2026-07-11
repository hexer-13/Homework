# Назва
#
# Частота
#
# Об'єм оперативної пам'яті
#
# Наявність DVD ROM
#
# Вартість
#
# Визначити кількість комп'ютерів з об'ємом оперативної пам'яті більше 10 Гбайт і надрукувати всі відомості про них.

class Computer:
    def __init__(self, name, frequency, ram, dvd_rom, cost):
        self.__name = name
        self.__frequency = frequency
        self.__ram = ram
        self.__dvd_rom = dvd_rom
        self.__cost = cost

    @property
    def name(self):
        return self.__name
    @property
    def frequency(self):
        return self.__frequency
    @property
    def ram(self):
        return self.__ram
    @property
    def dvd_rom(self):
        return self.__dvd_rom
    @property
    def cost(self):
        return self.__cost

    @name.setter
    def name(self, name):
        self.__name = name
    @frequency.setter
    def frequency(self, frequency):
        self.__frequency = frequency
    @ram.setter
    def ram(self, ram):
        self.__ram = ram
    @dvd_rom.setter
    def dvd_rom(self, dvd_rom):
        self.__dvd_rom = dvd_rom
    @cost.setter
    def cost(self, cost):
        self.__cost = cost

    def __str__(self):
        return f"{self.__name}, {self.__frequency}, {self.__ram}, {self.__dvd_rom}, {self.__cost}"