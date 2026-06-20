 # Створіть клас, який описує відгук до книги. Додайте до класу книги поле – список відгуків.
# Зробіть так, щоб при виведенні книги на екран за допомогою функції print також виводилися відгуки до неї.

class Book:
    def __init__(self, author, name, year, genre):
        self.author = author
        self.name = name
        self.year = year
        self.genre = genre
        self.reviews = []

    def __str__(self):
        return f'{self.author}, {self.name}, {self.year}, {self.genre}, {self.reviews}'

    def __repr__(self):
        return f'Book(name={self.name!r}, year={self.year!r}, genre={self.genre!r}, reviews={self.reviews})'

    def add_review(self, review):
        self.reviews.append(review)


class Review:
    def __init__(self, user_name, rate, review):
        self.user_name = user_name
        self.rate = rate
        self.review = review

    def __str__(self):
        return f'{self.user_name}, {self.rate}, {self.review}'

    def __repr__(self):
        return f'{self.user_name}, {self.rate}, {self.review}'





Book1 = Book('Author1', 'Booktitle1', 2000, "Horror")
Review1 = Review('User1', 1, "review1")
Book1.add_review(Review1)
print(Book1)
print(repr(Book1))