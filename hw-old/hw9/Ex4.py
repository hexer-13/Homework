def sum_recursion(start,end):
    if start > end:
        return 0
    if start == end:
        return start
    return start + sum_recursion(start + 1, end)




print(sum_recursion(1,5))