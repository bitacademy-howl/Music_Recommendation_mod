str1 = '01'
int1 = int(str1)
print(int1)

list1 = ['2000', '01', '02']
t1 = tuple(list1)
list2 = list(map(lambda x:int(x), list1))

print(type(list2), type(list2[0]), type(list2[1]), type(list2[2]))
print(list2[0],list2[1],list2[2])