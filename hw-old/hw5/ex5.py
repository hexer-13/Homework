from collections import deque
import collections

cort = tuple()

inp = input("Введіть перше число: ")
cort = (inp,)
while inp.isdigit():
    inp = input("Введіть наступне число: ")
    if inp.isdigit():
        cort = cort + (inp,)
if inp.isalpha():
    print("Було введено літеру")
else:
    sorted_cort = sorted(cort)
    print(sorted_cort)

