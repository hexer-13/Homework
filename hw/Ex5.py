def quadratic_equation(a,b,c):
    x1 = None
    x2 = None
    def calc_result(fa, fb, fc):
        nonlocal x1, x2
        D = fb ** 2 - 4 * fa * fc
        if D > 0:
            x1 = (-fb + D ** 0.5) / (2 * fa)
            x2 = (-fb - D ** 0.5) / (2 * fa)
        elif D == 0:
            x1 = -fb / (2 * fa)
            x2 = -fb / (2 * fa)
    calc_result(a, b, c)
    if x1 == None and x2 == None:
        print("Рівняння не має дійсних коренів")
    elif x1 != None and x2 == None:
        print("Рівняння має один корінь: x = ", x1)
    elif x1 == None and x2 != None:
        print("Рівняння має один корінь: x = ", x2)
    else:
        print("Рівняння має два корені: x1 =",x1,", x2 = ", x2)

print("Введіть коефіцієнти для квадратного рівняння (ax^2 + bx + c = 0):")
user_a = float(input("a = "))
user_b = float(input("b = "))
user_c = float(input("c = "))
if user_a == 0:
    print("Error")
quadratic_equation(user_a,user_b,user_c)