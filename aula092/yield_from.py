def t1():
    yield 1
    yield 2
    yield 3


def t2():
    yield from t1()
    yield 4
    yield 5
    yield 6

gen = t2()

for i in gen:
    print(i)