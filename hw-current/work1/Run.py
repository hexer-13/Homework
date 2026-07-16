from multiprocessing.connection import wait

from Functions import *

x = older_than_x(workers_list,60)
print_2(x)

x = older_than_x(67,"AAA")
print_2("AAA")