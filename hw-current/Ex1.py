# Прізвище
# Група
# Фізика
# Інформ
# Історія
#
# Визначити середній бал оцінок з фізики, кількість студентів з оцінкою 5 з інформатики та вивести відомості про них.

class Grades:
    def __init__(self, surname,group,physics,informatics,history):
        self.__surname = surname
        self.__group = group
        self.__physics = physics
        self.__informatics = informatics
        self.__history = history

    @property
    def surname(self):
        return self.__surname

    @property
    def group(self):
        return self.__group

    @property
    def physics(self):
        return self.__physics

    @property
    def informatics(self):
        return self.__informatics

    @property
    def history(self):
        return self.__history



Student1 = Grades("Surname1",)