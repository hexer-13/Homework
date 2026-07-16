from Class import *

# Визначити найдорожчий товар на складі та надрукувати всі відомості про нього.

def most_expensive(input_list):
    if not isinstance(input_list,list):
        print("Input must be a list")
        return None
    res = None
    try:
        for i in input_list:
            if res is None or i.price > res.price:
                res = i
    except Exception as e:
        print(e)
    return res