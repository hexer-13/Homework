# 2 Поля
# Прізвище
# Група
# Фізика
# Інформ
# Історія
# Визначити середній бал оцінок з всіх предметів,
# і вивести відомості про ня про студентів, середній бал яких більший за 4 яких більше 4.

class School:
    def __init__(self, surname, group, physics, informatics, history):
        self.surname = surname
        self.group = group
        self.physics = physics
        self.informatics = informatics
        self.history = history

    def __str__(self):
        return f'{self.surname}, {self.group}, {self.physics}, {self.informatics}, {self.history}'


s1 = School("sur1","A",12,12,12)
s2 = School("sur2","A",4,4,4)
s3 = School("sur3","B",10,11,12)
s4 = School("sur4","B",4,4,3)
s5 = School("sur5","C",1,7,5)
s6 = School("sur6","C",1,1,1)

students = [s1, s2, s3, s4, s5, s6]

def average_grade(student):
    total = (student.physics + student.informatics + student.history) / 3
    return total

print(average_grade(s1))

def average_above_number(students, number):
    for student in students:
        average = average_grade(student)
        if average > number:
            print(f'{student}, average - {average}')


average_above_number(students, 4)

