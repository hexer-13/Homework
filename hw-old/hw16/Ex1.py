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

    def __str__(self):
        return f"{self.surname}, {self.group}, {self.physics}, {self.informatics}, {self.history}"



Student1 = Grades("Surname1","A",5,5,5)
Student2 = Grades("Surname2","A",4,0,3)
Student3 = Grades("Surname3","B",3,5,1)
Student4 = Grades("Surname4","B",2,0,2)
Student5 = Grades("Surname5","C",1,5,4)

students = [Student1,Student2,Student3,Student4,Student5]

def average_grade(student_list,subject):
    total = 0
    subject = subject.lower()
    for student in student_list:
        match subject:
            case "physics":
                total += student.physics
            case "informatics":
                total += student.informatics
            case "history":
                total += student.history
            case _:
                return "Не має такого предмету"
        if student == student_list[-1]:
            return total/len(student_list)


def all_grade(student_list,subject,grade):
    total = 0
    list_res = []
    subject = subject.lower()
    for student in student_list:
        match subject:
            case "physics":
                if student.physics == grade:
                    total += 1
                    list_res.append(str(student))
            case "informatics":
                if student.informatics == grade:
                    total += 1
                    list_res.append(str(student))
            case "history":
                if student.history == grade:
                    total += 1
                    list_res.append(str(student))
            case _:
                return "Не має такого предмету"
        if student == student_list[-1] and list_res != []:
            return total, list_res
        elif student == student_list[-1]:
            return "Не має учнів з такою оцінкою"



print(average_grade(students,"physics"))
print(average_grade(students,"wrong"))
print(all_grade(students,"informatics",5))
print(all_grade(students,"history",10))