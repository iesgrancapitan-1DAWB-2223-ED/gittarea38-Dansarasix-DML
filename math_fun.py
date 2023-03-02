import math


def raiz(a, n):
    return a ** (1 / n)


def fact(n):
    f = 1
    for i in range(n):
        f *= (i + 1)
    return f


def calc_e(a):
    e = 1
    for i in range(a):
        i += 1
        e += 1 / fact(i)
    return e


def calc_pi(n):
    pi = 0
    for i in range(n):
        a = (-1) ** i
        b = (2 ** i) + 1
        pi += a / b
    return pi


def sen(x):
    sen = 0
    for i in range(85):
        a = round(((-1) ** i) * (x ** (2 * i + 1)), 16)
        b = round(fact(2 * i + 1))
        sen += a / b
    return round(sen, 16)


def asen(x):
    asen = 0
    for i in range(85):
        a = fact(2 * i)
        b = (4 ** i) * ((fact(i)) ** 2) + (2 * i + 1)
        c = x ** (2 * i + 1)
        asen += (a / b) * c
    return asen


e = calc_e(16)
au = (1 + raiz(5, 2)) / 2
pi = calc_pi(16) * 10.6751386254715749
print(pi)


def log(n, log_base):
    log = n
    C = 0
    m = 0
    M = 0

    while log > log_base:
        log = log / log_base
        C = C + 1

    m = str(m) + "."

    for i in range(0, 16):
        log = log ** 10
        while log > 10:
            log = log / 10
            M = M + 1

        m = str(m) + str(M)
        M = 0

    log = float(C) + float(m)

    return log


def log_nep(x):
    ln = log(x, 10) / log(e, 10)
    return ln


def fibonacci(a):
    f0, f1 = 0, 1
    for i in range(a):
        print(f1)
        f0, f1 = f1, f0 + f1
