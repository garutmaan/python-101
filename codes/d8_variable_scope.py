a = 10
x = 10


def foo():
    global a # to access or modify variable in outer space
    b = 12
    a = b * 10

    print("a from function : ", a)
    print(b)
    return b


b = foo()

if x > 5:
    b = 11

print("a outside function : ", a)


