"""
Найдите такое число x, что , с точностью не менее 6 знаков после точки.

Входные данные
В единственной строке содержится вещественное число 1.0≤C≤10^10.

Выходные данные
Выведите одно число — искомый x.
"""
import sys
import math


def bin_search(c, f, eps=5e-7):
    l = 0
    r = 10 ** 5
    while r - l > eps:
        m = (l + r) / 2
        if f(m) < c:
            l = m
        else:
            r = m
    return r


if __name__ == '__main__':
    raw_input = sys.stdin.read().splitlines()
    c = float(raw_input[0])
    f = lambda x: x ** 2 + math.sqrt(x)
    print(round(bin_search(c, f), 6))
