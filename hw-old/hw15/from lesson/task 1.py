# Поля
# Прізвище
# Амплуа
# Вік
# Кількість ігор
# Кількість голів
# Визначити найкращого форварда, і вивести відомості про футболістів, які зіграли менше 5-ти ігор.

class Footbal():
    def __init__(self, lastname, amplua, age, count_of_games, count_of_goals):
        self.lastname = lastname
        self.amplua = amplua
        self.age = age
        self.count_of_games = count_of_games
        self.count_of_goals = count_of_goals

    def __str__(self):
        return f"{self.lastname}, {self.amplua}, {self.age}, {self.count_of_games}, {self.count_of_goals}"


f1 = Footbal('ln1','for',27, 1, 7)
f2 = Footbal('ln2','wor',17, 7, 0)
f3 = Footbal('ln3','for',28, 5, 1)
f4 = Footbal('ln4','zah',37, 1, 3)
f5 = Footbal('ln5','for',47, 3, 2)

footbolist = [f1, f2, f3, f4, f5]

def best_forward(footbolist,aplua):
    best_f = None
    max_goal = -1
    for gravec in footbolist:
        if gravec.amplua == aplua and gravec.count_of_goals > max_goal:
            max_goal = gravec.count_of_goals
            best_f = gravec
    return best_f

print(best_forward(footbolist,'for'))

def five_games(footbolist,count_of_games):
    for player in footbolist:
        if player.count_of_games >= count_of_games:
            print(player)

five_games(footbolist,5)