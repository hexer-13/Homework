# OOP.
# 1
# Поля
# Найменування
# Кількість
# Ціна
# Виробник
# Дата_надходження_на_склад
#
# Визначити кількість усіх товарів, кількість яких більша за 5 і вивести відомості про ці товари
# функция повертаэ лист
# класс конкретний продукт успадкувати вид продакт
class Product:
    def __init__(self, name, amount, price, manufacturer, date):
        self.name = name
        self.amount = amount
        self.price = price
        self.manufacturer = manufacturer
        self.date = date

    def __str__(self):
        return (f'{self.name}, {self.amount}, {self.price}, {self.manufacturer}, {self.date}')

class Knife(Product):
    def __init__(self,name,amount,price,manufacturer,date,sharpness,material):
        super().__init__(name,amount,price,manufacturer,date)
        self.sharpness = sharpness
        self.material = material

    def __str__(self):
        return (f'{self.name}, {self.amount}, {self.price}, {self.manufacturer}, {self.date}, {self.sharpness}, {self.material}')

def over_number(products,number):
    filtered_list = []
    for product in products:
        if product.amount >= number:
            filtered_list.append(product.name)
            filtered_list.append(product.amount)
            print(product)
    return filtered_list

product1 = Product("name1",3,100,"man1",2000)
product2 = Product("name2",4,200,"man2",2001)
product3 = Product("name3",5,300,"man3",2002)
knife1 = Knife("name4",4,400,"man4",2003,1,"iron")
knife2 = Knife("name5",5,500,"man5",2004,2,"steel")
knife3 = Knife("name6",6,600,"man6",2005,3,"titanium")

product_list = [product1,product2,product3,knife1,knife2,knife3]
print(over_number(product_list,5))