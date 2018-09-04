# Asterisk 예제 받을 때 ** 는 가변인자를 dictionary 형태로 받음
# 호출 시에는 각 인자의 값들을 (x=x.value, y=y.value, ....) 형태로 호출하여야 함.

def print_param2(**kwargs):
    print(kwargs)
    print(kwargs.keys())
    print(kwargs.values())

    for name, value in kwargs.items():
        print("%s : %s" % (name, value))
#
aa = print_param2(first='a', second='b', third='c', fourth='d')
