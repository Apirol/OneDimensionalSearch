from math import sqrt
from Init import InitReport

SQRT5 = sqrt(5)

def function(x):
    return pow(x - 8, 2)


def bisection_method(a, b, eps, filename):
    numberOfCalc = 0
    report = InitReport(filename)
    handle = report.get_handle()

    while (abs(a - b) > eps):
        x1 = (a + b - eps / 2) / 2
        x2 = (a + b + eps / 2) / 2

        f1 = function(x1)
        f2 = function(x2)

        numberOfCalc += 2

        if (f1 < f2):
            b = x2
        else:
            a = x1

        handle.write("{:f}\t{:f}\t""{:f}\t{:f}\t\t""{:f}\t\t\t{:f}\t\t""{:f}\t\t\t\t{:f}\n".format(x1, x2, f1, f2, a, b,
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

        handle.write("{:f}\t{:f}\t""{:f}\t{:f}\t\t""{:f}\t\t\t{:f}\t\t""{:f}\t\t\t\t{:f}\n"
                     .format(x1, x2, f1, f2, a, b, current_lenght, current_lenght / (b - a)))

        current_lenght = b - a

    return numberOfCalc, a


def Fibonacci(a, b, eps, filename):
    numberOfCalc = 0
    current_lenght = b - a
    report = InitReport(filename)
    handle = report.get_handle()

    return numberOfCalc, (a + b) / 2


