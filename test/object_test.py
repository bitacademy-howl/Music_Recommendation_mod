class a:
    id = 123
    name = "이희웅"

    def __str__(self):
        return "{0}, {1}".format(self.name, self.id)

a.id = 'aaa'
print(a)

b = a()
print(b)