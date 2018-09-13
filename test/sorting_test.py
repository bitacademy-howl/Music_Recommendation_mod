# sort()
# sort() : 현재 리스트를 정렬

a = [3,5,7,8,2,6]
a.sort()

# sorted()
# sorted() : 함수의 인자로 들어온 리스트를 정렬해서 반환

a = [3,5,7,8,2,6]
b = sorted(a) # b에 정렬된 리스트가 새로 생성됨


########################################################################################################################
# key 매개변수 이용하기
# key매개변수를 이용하여 비교하기전에 함수를 정의 할 수 있다.
# key매개변수는 하나의 인자를 갖는 함수여야하며 정렬에 사용할 key를 반환해야한다.

# 튜플(tuple)을 사용하는 경우

example_tuples = [ ('A', 3, 'a'), ('B', 1, 'b'), ('C', 2, 'c') ]

# 정렬
example_tuples.sort(key = lambda element : element[1])
########################################################################################################################

########################################################################################################################
# ******************************************************************************************************************** #
########################################################################################################################
# 객체(Object)를 사용하는 경우

class Example:

    def __init__(self, big, number, small):
        self.big = big
        self.number = number
        self.small = small

    def __repr__(self):
        return "big : {0}, number : {1}, small : {2}".format(self.big, self.number, self.small)

example_objects = [ Example('A', 3, 'a'), Example('B', 1, 'b'), Example('C', 2, 'c') ]

# 정렬
example_objects.sort(key = lambda object : object.number)
print(example_objects)
########################################################################################################################
# Good
########################################################################################################################