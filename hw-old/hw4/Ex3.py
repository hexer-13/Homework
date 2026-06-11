#Використовуючи вкладені цикли та функції print(‘*’, end=’’), print(‘ ‘, end=’’) та print()
# виведіть на екран прямокутний трикутник

print("*", end="")
for i in range(1,11):
    print()
    print("*", end="")
    for i in range(1,i):
        print(" ", end="")
    print("*", end="")
print()
for i in range(i+3):
    print("*", end="")

