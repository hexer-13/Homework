from Functions import *
from Objects import *



print_info(biggest_screen(item_list))
print_info(smallest_screen(item_tuple))
print_info(cheapest_laptop(item_set))
print_info(most_expensive_laptop(item_list))
print_info(most_ram(item_tuple))
print_info(least_ram(item_set))

print("------------------------")

save_info(biggest_screen(item_list))
print_info(read_info(1))
save_info(smallest_screen(item_list))
print_info(read_info(2))