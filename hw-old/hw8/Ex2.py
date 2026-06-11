def square(number):
    return number * number


def add_13(number):
    return number + 13

print(" X  | X^2  | X+13 ")
for i in range(-10,12,1):
    print("-" * 20)
    print(i,"|",square(i/2),"|",add_13(i/2))