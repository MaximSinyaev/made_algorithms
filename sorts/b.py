"""
Дан небольшой массив целых чисел. Ваша задача — отсортировать его в порядке
неубывания.

Входные данные

В первой строке входного файла содержится число N (1≤N≤1000) — количество
элементов в массиве. Во второй строке находятся N целых чисел, по модулю не
превосходящих 109.

Выходные данные

В выходной файл надо вывести этот же массив в порядке неубывания, между любыми
двумя числами должен стоять ровно один пробел.
"""

if __name__ == '__main__':
    n = int(input())
    ar = [int(_) for _ in input().split()]
    for i in range(n):
        j = i
        while j > 0 and ar[j - 1] > ar[j]:
            ar[j - 1], ar[j] = ar[j], ar[j - 1]
            j -= 1
    print(*ar)
