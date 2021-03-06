"""
Даны два массива. Первый массив отсортирован по неубыванию, второй массив содержит запросы — целые числа. Для каждого
запроса выведите число из первого массива наиболее близкое к числу в этом запросе. Если таких несколько, выведите
меньшее из них.

Входные данные
В первой строке входных данных содержатся числа n и k (0 < n, k ≤ 105). Во второй строке задаются n чисел
первого массива, отсортированного по неубыванию, а в третьей строке – k чисел второго массива. Каждое число в обоих
массивах по модулю не превосходит 2·109 .

Выходные данные
Для каждого из k чисел выведите в отдельную строку число из первого массива, наиболее близкое к данному. Если таких
несколько, выведите меньшее из них.
"""


def upper_bound(a, x):
    l = -1
    r = len(a)
    while l < r - 1:
        m = (l + r) // 2
        if x <= a[m]:
            r = m
        else:
            l = m
    return r


if __name__ == '__main__':
    n, k = [int(_) for _ in input().split()]
    ar = [int(_) for _ in input().split()]
    queries = [int(_) for _ in input().split()]
    for q in queries:
        # print(lower_bound(ar, q, 0, n))
        if q <= ar[0]:
            print(ar[0])
        elif q >= ar[-1]:
            print(ar[-1])
        else:
            rb = upper_bound(ar, q)
            lb = rb - 1
            # print(q, lb, rb)
            if lb > -1 and abs(q - ar[lb]) > abs(ar[rb] - q):
                print(ar[rb])
            else:
                print(ar[lb])
