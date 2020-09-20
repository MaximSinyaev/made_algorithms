"""
Дан массив целых чисел. Ваша задача — отсортировать его в порядке неубывания.

Входные данные

В первой строке входного файла содержится число N (1≤N≤100000) — количество
элементов в массиве. Во второй строке находятся N целых чисел, по модулю не
превосходящих 109.

Выходные данные

В выходной файл надо вывести этот же массив в порядке неубывания, между любыми
двумя числами должен стоять ровно один пробел.

Сортировка слиянием
"""


def merge(left, right):
    left_len = len(left)
    right_len = len(right)
    i = 0
    j = 0
    res = [0] * (left_len + right_len)
    while (i + j) < (left_len + right_len):
        if i < left_len and j < right_len and left[i] <= right[j]:
            res[i + j] = left[i]
            i += 1
        elif j < right_len:
            res[i + j] = right[j]
            j += 1
        else:
            res[i + j] = left[i]
            i += 1
    return res


def merge_sort(array):
    array_len = len(array)
    if array_len > 1:
        left = array[:(array_len + 1) // 2]
        right = array[(array_len + 1) // 2:]
        res = merge(merge_sort(left), merge_sort(right))
    else:
        return array
    return res


if __name__ == '__main__':
    n = int(input())
    ar = [int(_) for _ in input().split()]
    print(*merge_sort(ar))
    # a = [1, 4, 7]
    # b = [1, 2, 3, 5, 8]
    # print(merge(a, b))
    # print(merge_sort([1, 7, 2, 8]))
