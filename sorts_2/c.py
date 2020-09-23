"""
Дано n строк, выведите их порядок после k фаз цифровой сортировки.
В этой задаче требуется реализовать цифровую сортировку.

Входные данные
В первой строке входного файла содержится число n — количество строк, m — их длина и k – число фаз цифровой сортировки
(1≤n≤1000, 1≤k≤m≤1000). В следующих n строках находятся сами строки.

Выходные данные
Выведите строки в порядке в котором они будут после k фаз цифровой сортировки.
"""
from collections import deque


def count_sort_by_key(array: list, indexes: list, key: int):
    cnt = [deque() for _ in range(26)]
    result = [0] * len(array)
    for i in indexes:
        val = ord(array[i][key]) - ord('a')
        cnt[val].append(i)
    i = 0
    result_iter = 0
    while i < len(cnt):
        while cnt[i]:
            result[result_iter] = cnt[i].popleft()
            result_iter += 1
        if not cnt[i]:
            i += 1
    return result


def digit_sort(array: list, m: int, k: int):
    indexes = list(range(len(array)))
    m -= 1
    for key_num in range(m, m - k, -1):
        indexes = count_sort_by_key(array, indexes, key_num)
    array = [array[i] for i in indexes]
    return array


if __name__ == '__main__':
    n, m, k = [int(_) for _ in input().split()]
    array = list()
    for _ in range(n):
        array.append(input())
    print(*digit_sort(array, m, k), sep='\n')
