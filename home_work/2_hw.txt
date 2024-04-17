def task_1() -> str:
    a = 3
    print(a, " относится к типу ", type(a))
    b = 20.002
    print(b, " относится к типу ", type(b))
    c = "Яблоко"
    print(c, " относится к типу ", type(c))
    d = [2, 4, 6]
    print(d, " относится к типу ", type(d))
    e = True
    print(e, " относится к типу ", type(e))
    return c


print(task_1())


def task_2() -> list:
    a = [1, 2, 3, 5, 8, 13, 21]
    print("a[0:3] = ", a[0:3])
    return a


print(task_2())


def task_3(x: int) -> int:
    return x**2


print(task_3(4))

