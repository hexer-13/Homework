# Продавець
# Найменування
# Кількість
# Ціна
# Дата_продажу
# Визначити кількість товарів, які продані менше року тому і вивести відомості про них

class Sell:
    def __init__(self,seller,name,amount,price,months_ago):
        self.seller = seller
        self.name = name
        self.amount = amount
        self.price = price
        self.months_ago = months_ago

    def __str__(self):
        return f'{self.seller},{self.name},{self.amount},{self.price},{self.months_ago}'


it1 = Sell("Guy1","Item1",1,100,3)
it2 = Sell("Guy2","Item2",2,200,6)
it3 = Sell("Guy3","Item3",3,300,9)
it4 = Sell("Guy4","Item4",4,400,12)
it5 = Sell("Guy5","Item5",5,500,15)

items = [it1,it2,it3,it4,it5]

def last_year_sales(items):
    for item in items:
        if item.months_ago < 12:
            print(item)

last_year_sales(items)