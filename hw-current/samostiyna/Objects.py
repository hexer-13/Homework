
from Class_apple import *

item1 = Laptop("NotApple", 99,1000,2)
item2 = Apple("Apple", 1,2000,2,"Model1","Processor1000")
item3 = Laptop("Pear", 30,1,3)
item4 = Apple("Apple", 40,99000,4,"Model2","Processor2000")
item5 = Laptop("Applen't", 50,5000,999999)
item6 = Apple("Apple", 60,6000,1,"Model3","Processor3000")

item_list = [item1, item2, item3, item4, item5]
item_tuple = (item1, item2, item3, item4, item5)
item_set = {item1, item2, item3, item4, item5}