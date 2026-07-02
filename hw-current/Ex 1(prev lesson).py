import datetime

class Book:
    def __init__(self, author, pages, quantity, date):
        self.__author = author
        self.__pages = pages
        self.__quantity = quantity
        self.__date = date

    @property
    def author(self):
        return self.__author

    @property
    def pages(self):
        return self.__pages

    @property
    def quantity(self):
        return self.__quantity

    @property
    def date(self):
        return self.__date

    def __str__(self):
        return f"{self.__author}, {self.__pages}, {self.__quantity}, {self.__date}"



book1 = Book("author1", 50, 5, datetime.date(2026, 6, 1))
book2 = Book("author2", 100, 10, datetime.date(2026, 6, 2))
book3 = Book("author3", 150, 15, datetime.date(2026, 6, 3))
book4 = Book("author4", 200, 20, datetime.date(2026, 6, 4))
book5 = Book("author5", 300, 30, datetime.date(2026, 6, 5))

books_list = [book1, book2, book3, book4, book5]

def books_with_pages_above(books,page_number):
    res_list = []
    try:
        for book in books:
            if book.pages > page_number:
                res_list.append(str(book))

        return res_list

    except TypeError:
        return "Не правильне введення"

    except Exception as e:
        print(e)



print(books_with_pages_above(books_list,150))
print(books_with_pages_above(books_list,"a"))