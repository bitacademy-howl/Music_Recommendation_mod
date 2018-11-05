class a:
    id = 123
    name = "이희웅"

    def __str__(self):
        return "{0}, {1}".format(self.name, self.id)

a.id = 'aaa'
print(a)

b = a()
print(b)


li = list()
li.append("asd")
li.append("123")
li.append(12333)

print(li)

print(li[0])
print(li)

# dict1 = dict()

dict1 = dict()


list1 = [1,2,3]
list2 = [3,4,5]

for i in range(len(list1)):
    dict1.update([(list1[i], list2[i])])

print(dict1)