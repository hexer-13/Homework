from Functions import *
from Objects import *

x = average_salary(worker_list)
y = salary_more_than_x(worker_list,x)
a = older_than_x(worker_list,30)
b = older_than_x(y,30)

print_2(y)
input()
print_2(a)
input()
print_2(b)
