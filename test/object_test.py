class a:
    id = 123
    name = "이희웅"

    def __str__(self):
        return "{0}".format(self.name, self.id)