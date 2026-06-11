List_1 = [1,2,4,5,7,8,10,11,14,1,1,2]
List_2 = [1,3,4,6,7,9,10,12,13,1,1,3]

set1 = set(List_1)
set2 = set(List_2)

print(set1.difference(set2))
print(set2.difference(set1))