# Створіть програму, яка малює на екрані прямокутник із зірочок заданою користувачем ширини та висоти.
x = int(input("Введіть ширину: "))
y = int(input("Введіть висоту: "))

for i in range(1,x+1):
    print("*", end="")
for i in range(1,y+1):
    print()
    print("*", end="")
    for i in range(1,x-1):
        print(" ", end="")
    print("*", end="")
print()
for i in range(1,x+1):
    print("*", end="")