print("Введіть параметри кожного кольору в RGB (в діапазоні від 0 до 255)")
red = int(input("Введіть червоний (R): "))
green = int(input("Введіть зелений (G): "))
blue = int(input("Введіть синій (B): "))
rgb=(red,green,blue)
if max(rgb) > 255 or min(rgb) < 0:
    print("Не правильні параметри RGB")
else:
    print("RGB:", rgb)