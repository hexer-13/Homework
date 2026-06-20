# Створіть клас, який описує книгу. Він повинен містити інформацію про автора, назву, рік видання та жанр.
# Створіть кілька різних книжок. Визначте для нього методи _repr_ та _str_.

class Book:
    def __init__(self, author, name, year, genre):
        self.author = author
        self.name = name
        self.year = year
        self.genre = genre

    def __str__(self):
        return f'{self.author}, {self.name}, {self.year}, {self.genre}'

    def __repr__(self):
        return f'Book(name={self.name!r}, year={self.year!r}, genre={self.genre!r})'
Book1 = Book('Author1', 'Booktitle1', 2000, "Horror")

print(Book1)
print(repr(Book1))

