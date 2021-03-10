from math import sqrt
from file_init import FileInit
import numpy as np

SQRT5 = sqrt(5)


def function(x):
    return pow(x - 8, 2)


def bisection_method(a, b, eps, filename):
    number_of_calc = 0
    current_length = b - a
    report = FileInit(filename)
    report.write_title_for_method()
    handle = report.get_handle()

    while abs(a - b) > eps:
        x1 = (a + b - eps / 2) / 2
        x2 = (a + b + eps / 2) / 2

        f1 = function(x1)
        f2 = function(x2)
        i: int = 0

        number_of_calc += 2

        if f1 < f2:
            b = x2
        else:
            a = x1

        i += 1
        handle.write("{:d}\t{:f}\t{:f}\t""{:f}\t{:f}\t""{:f}\t{:f}\t""{:f}\t{:f}\n".format(i, x1, x2, f1, f2, a, b,
                                       current_length, current_length / (b - a)))

        current_length = b - a

    report.close_handle()
    return number_of_calc, (a + b) / 2


def golden_ratio(a, b, eps, filename):
    number_of_calc = 0
    current_length = b - a
    report = FileInit(filename)
    report.write_title_for_method()
    handle = report.get_handle()

    global SQRT5
    x1 = a + (3 - SQRT5) / 2 * (b - a)
    x2 = a + (SQRT5 - 1) / 2 * (b - a)

    f1 = function(x1)
    f2 = function(x2)
    i: int = 0

    while abs(a - b) > eps:
        number_of_calc += 1

        if f1 < f2:
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
                     .format(i, x1, x2, f1, f2, a, b, current_length, current_length / (b - a)))

        current_length = b - a

    report.close_handle()
    return number_of_calc, a


def read_massive(filename):
    return np.loadtxt(filename, dtype=np.int)


def fibonacci(a, b, eps, filename):
    FIBONACCI = read_massive("fibonacci_numbers.txt")
    n: int = 0
    number_of_calc = 0
    current_length = b - a
    report = FileInit(filename)
    report.write_title_for_method()
    handle = report.get_handle()

    while FIBONACCI[n] < current_length / eps:
        n += 1

    n -= 3
    print("Число n = " + str(n))
    x1 = a + FIBONACCI[n] / FIBONACCI[n + 2] * (b - a)
    x2 = a + b - x1
    f1 = function(x1)
    f2 = function(x2)
    i: int = 0

    while number_of_calc <= n:
        number_of_calc += 1
        if f1 < f2:
            b = x2
            x2 = x1
            x1 = a + FIBONACCI[n - number_of_calc + 1] / FIBONACCI[n - number_of_calc + 3] * (b - a)
            f2 = f1
            f1 = function(x1)
        else:
            a = x1
            x1 = x2
            x2 = a + FIBONACCI[n - number_of_calc + 2] / FIBONACCI[n - number_of_calc + 3] * (b - a)
            f1 = f2
            f2 = function(x2)

        i += 1
        handle.write("{:d}\t{:f}\t{:f}\t""{:f}\t{:f}\t""{:f}\t{:f}\t""{:f}\t{:f}\n"
                     .format(i, x1, x2, f1, f2, a, b, current_length, current_length / (b - a)))

        current_length = b - a

    report.close_handle()
    print(x1, x2)
    return number_of_calc, a


def search_minimal_segment(x0, eps, filename):
    number_of_calc = 0
    report = FileInit(filename)
    report.write_title_for_search()
    handle = report.get_handle()
    h: float = 0
    first_x: float = x0
    current_x: float = 0
    next_x: float = 0
    first_f: float = function(first_x)

    if first_f > function(first_x + eps):
        current_x = first_x + eps
        h = eps
    elif first_f > function(first_x - eps):
        current_x = first_x - eps
        h = - eps

    h = 2 * h
    current_f = function(current_x)
    next_f = function(current_x + h)
    while current_f > next_f:
        handle.write("{:f}\t{:f}\n".format(current_x, current_f))
        h = 2 * h
        number_of_calc += 1

        next_x = current_x + h
        first_x = current_x
        current_x = next_x

        current_f = next_f
        next_f = function(next_x)

    report.close_handle()
   ## print(first_x, next_x, number_of_calc)
