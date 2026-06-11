def sum_recursion(start,end):
    if start > end:
        return 0
    # Базовий випадок: якщо числа рівні
    if start == end:
        return start
    # Рекурсивний випадок: поточне число + сума для решти проміжку
    return start + sum_recursion(start + 1, end)




print(sum_recursion(1,5))