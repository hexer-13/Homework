from collections import namedtuple

Marks = namedtuple('Оцінки', 'Алгебра, Геометрія, Історія, Інформатика, Географія')
marks1 = Marks(1, 2, 3, 4, 5)
print("У Колі наступний табель:", marks1)

marks2 = Marks(100, 100, 100, 100, 100)
print("У Насті наступний табель:", marks2)

marks3 = Marks(67, 67, 67, 67, 67)
print("У Максима наступний табель:", marks3)