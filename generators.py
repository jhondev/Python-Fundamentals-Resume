#Subject to go deep

def gen123():
    yield 1
    yield 2
    yield 3

def lucas():
    yield 2
    a = 2
    b = 1
    while True:
        yield b
        a, b = b, a + b

g = gen123()

for value in g:
    print(value)

h = gen123()
print(next(h))