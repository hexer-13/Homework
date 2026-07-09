# Прізвище
# Вік
# Кількість ігор
# Кількість пропущених шайб
# Визначити середній вік хокеїстів і вивести відомості про хокеїстів, вік яких понад 25 років.
from email import generator


class Hokeist:
    def __init__(self, name, age, games_amount, missed):
        self.__name = name
        self.__age = age
        self.__games_amount = games_amount
        self.__missed = missed

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def games_amount(self):
        return self.__games_amount

    @property
    def missed(self):
        return self.__missed

    def __str__(self):
        return f"|Name: {self.__name}|Age: {self.__age}|Games played: {self.__games_amount}|Goals missed: {self.__missed}|"

hokey1 = Hokeist("Name1",23,1,1)
hokey2 = Hokeist("Name2",24,2,2)
hokey3 = Hokeist("Name3",25,3,3)
hokey4 = Hokeist("Name4",26,4,4)
hokey5 = Hokeist("Name5",27,5,5)

players = [hokey1, hokey2, hokey3, hokey4, hokey5]

def find_average_age(input_list):
    res = 0
    try:
        for player in players:
           res += player.age
        res/=len(players)
        return res

    except TypeError:
        return "Wrong Input"

    except Exception as e:
        return e


def players_older_then(input_list,input_age):
    res = []
    try:
        for player in input_list:
            if player.age >= input_age:
                res.append(str(player))

        return res

    except TypeError:
        return "Wrong Input"

    except Exception as e:
        return e

def print2(input_list):
    try:
        gen = (item for item in input_list)
        for i in input_list: print(next(gen))
    except TypeError:
        print("Wrong Input")


print(find_average_age(players))
print(players_older_then(players,25))
print2(players_older_then(players,25))
print("")
print2(players)