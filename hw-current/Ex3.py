def count_ways(n):
    if n==1 or n ==2:
        return 1
    elif n<0:
        pass
    else:
        return count_ways(n-1) + count_ways(n-2)


num = int(input())
print("На сходинку", num, "можна піднятися", count_ways(num+1),"способами")
