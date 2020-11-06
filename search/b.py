"""
Дан массив из n целых чисел. Все числа от −10^9 до 10^9.

Нужно уметь отвечать на запросы вида «Cколько чисел имеют значения от l до r»?

Входные данные
Число n (1≤n≤10^5). Далее n целых чисел. Затем число запросов k (1≤k≤10^5). Далее k пар чисел l,r (−109≤l≤r≤10^9)
— собственно запросы.

Выходные данные
Выведите k чисел — ответы на запросы.
"""
import sys


def lower_bound(a, x):
    l = -1
    r = len(a)
    while l < r - 1:
        m = (l + r) // 2
        if x <= a[m]:
            r = m
        else:
            l = m
    return r


def upper_bound(a, x):
    l = -1
    r = len(a)
    while l < r - 1:
        m = (l + r) // 2
        if x < a[m]:
            r = m
        else:
            l = m
    return r


if __name__ == '__main__':
    raw_input = sys.stdin.read().splitlines()
    n = int(raw_input[0])
    ar = [int(_) for _ in raw_input[1].split()]
    ar.sort()
    k = int(raw_input[2])
    for i in range(k):
        lower, upper = [int(_) for _ in raw_input[3 + i].split()]
        left_upper_bound = lower_bound(ar, lower)
        right_upper_bound = upper_bound(ar, upper)
        # print(left_upper_bound, right_upper_bound)
        print(right_upper_bound - left_upper_bound, end=' ')
    print()
