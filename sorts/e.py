"""
Дан массив целых чисел. Ваша задача — отсортировать его в порядке неубывания.

Входные данные

В первой строке входного файла содержится число N (1≤N≤100000) — количество
элементов в массиве. Во второй строке находятся N целых чисел, по модулю не
превосходящих 109.

Выходные данные

В выходной файл надо вывести этот же массив в порядке неубывания, между любыми
двумя числами должен стоять ровно один пробел.

Быстрая сортировка
"""
import random


def qsort_(array):
    if len(array) <= 1:
        return array
    pivot = array[random.randint(0, len(array) - 1)]
    less, equal, greater = list(), list(), list()
    for i in array:
        if i < pivot:
            less.append(i)
        elif i == pivot:
            equal.append(i)
        else:
            greater.append(i)
    return qsort_(less) + equal + qsort_(greater)


if __name__ == '__main__':
    n = int(input())
    ar = [int(_) for _ in input().split()]
    # qsort(0, n, ar)
    # print(*ar)
    print(*qsort_(ar))
