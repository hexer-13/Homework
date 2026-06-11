def imt_calc(weight,height):
    height_meters = height / 100
    imt = weight / (height_meters ** 2)
    if imt < 18.5:
        print("Недостатня вага, ІМТ =", imt)
    elif imt < 25:
        print("Маса тіла в нормі, ІМТ =", imt)
    else:
        print("Слідкуйте за фігурою, ІМТ =", imt)


while True:
    user_input = input("Введіть вашу вагу та ріст у сантиметрах через пробіл, або off щоб війти з програми: ")
    if user_input == "off":
        break
    weight,height = user_input.split(" ")
    imt_calc(int(weight),int(height))