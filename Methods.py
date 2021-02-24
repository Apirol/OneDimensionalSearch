from math import sqrt, log
from Init import InitReport

SQRT5 = sqrt(5)

def function(x):
    return pow(x - 8, 2)


def bisection_method(a, b, eps, filename):
    numberOfCalc = 0
    current_lenght = b - a
    report = InitReport(filename)
    handle = report.get_handle()

    while (abs(a - b) > eps):
        x1 = (a + b - eps / 2) / 2
        x2 = (a + b + eps / 2) / 2

        f1 = function(x1)
        f2 = function(x2)
        i: int = 0

        numberOfCalc += 2

        if (f1 < f2):
            b = x2
        else:
            a = x1

        i += 1
        handle.write("{:d}\t{:f}\t{:f}\t""{:f}\t{:f}\t""{:f}\t{:f}\t""{:f}\t{:f}\n".format(i, x1, x2, f1, f2, a, b,
                                       current_lenght, current_lenght / (b - a)))

        current_lenght = b - a

    return numberOfCalc, (a + b) / 2


def golden_ratio(a, b, eps, filename):
    numberOfCalc = 0
    current_lenght = b - a
    report = InitReport(filename)
    handle = report.get_handle()

    global SQRT5
    x1 = a + (3 - SQRT5) / 2 * (b - a)
    x2 = a + (SQRT5 - 1) / 2 * (b - a)

    f1 = function(x1)
    f2 = function(x2)
    i: int = 0

    while (abs(a - b) > eps):
        numberOfCalc += 1

        if (f1 < f2):
            b = x2
            x2 = x1
            x1 = a + (3 - SQRT5) / 2 * (b - a)
            f2 = f1
            f1 = function(x1)
        else:
            a = x1
            x1 = x2
            x2 = a + (SQRT5 - 1) / 2 * (b - a)
            f1 = f2
            f2 = function(x2)

        i += 1
        handle.write("{:d}\t{:f}\t{:f}\t""{:f}\t{:f}\t""{:f}\t{:f}\t""{:f}\t{:f}\n"
                     .format(i, x1, x2, f1, f2, a, b, current_lenght, current_lenght / (b - a)))

        current_lenght = b - a

    return numberOfCalc, a


def calc_fibonacci(n: int):
    return pow((1 + SQRT5) / 2, n) / SQRT5


def fibonacci(a, b, eps, filename):
    numberOfCalc = 0
    current_lenght = b - a
    report = InitReport(filename)
    handle = report.get_handle()

    n = round(log(SQRT5 * (b - a) / eps) / log((1 + SQRT5) / 2))
    x1 = a + calc_fibonacci(n) / calc_fibonacci(n + 2) * (b - a)
    x2 = a + calc_fibonacci(n + 1) / calc_fibonacci(n + 2) * (b - a)
    f1 = function(x1)
    f2 = function(x2)
    i: int = 0

    while (abs(a - b) > eps):
        numberOfCalc += 1

        if (f1 < f2):
            b = x2
            x2 = x1
            x1 = a + calc_fibonacci(n - numberOfCalc - 1) / calc_fibonacci(n - numberOfCalc + 1) * (b - a)
            f2 = f1
            f1 = function(x1)
        else:
            a = x1
            x1 = x2
            x2 = a + calc_fibonacci(n - numberOfCalc) / calc_fibonacci(n - numberOfCalc + 1) * (b - a)
            f1 = f2
            f2 = function(x2)

        i += 1
        handle.write("{:d}\t{:f}\t{:f}\t""{:f}\t{:f}\t\t""{:f}\t\t\t{:f}\t\t""{:f}\t\t\t\t{:f}\n"
                     .format(i, x1, x2, f1, f2, a, b, current_lenght, current_lenght / (b - a)))

        current_lenght = b - a

    return numberOfCalc, a


def search_minimal_segment(x0, eps, filename):
    numberOfCalc = 0
    report = InitReport(filename)
    handle = report.get_handle()
    h: float = 0
    x1: float = 0
    x2: float = 0
    f0: float = function(x0)

    if f0 > function(x0 + eps):
        x1 = x0 + eps
        h = eps
    elif function(x0) > function(x0 - eps):
        x1 = x0 - eps
        h = - eps

    x2 = x1 + h
    f1 = function(x1)
    f2 = function(x2)

    while f1 > f2:
        h = 2 * h
        numberOfCalc += 1
        x0 = x1
        f0 = f1
        x1 = x2
        f1 = f2
        x2 = x1 + h
        f2 = function(x2)

    print(x0, x1)




