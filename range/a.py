"""
Вам нужно научиться отвечать на запрос «сумма чисел на отрезке».

Массив не меняется. Запросов много. Отвечать на каждый запрос следует за .
Входные данные

Размер массива — n и числа x, y, a0, порождающие массив a:

Далее следует количество запросов m и числа z, t, b0, порождающие массив b: .

Массив c строится следующим образом: .

Запросы: i-й из них — найти сумму на отрезке от min(c2i,c2i+1) до max(c2i,c2i+1) в массиве a.

Ограничения: 1≤n≤107, 0≤m≤107. Все числа целые от 0 до 21^6. t может быть равно -1.
Выходные данные

Выведите сумму всех сумм.
"""
import sys

AR_MOD = 2 ** 16
B_MOD = 2 ** 30

def count_prefix_sum(n, x, y, a0):
    prev_a = a0
    prefix_sum = [a0] * n
    for i in range(1, n):
        next_a = (x * prev_a + y) % AR_MOD
        prefix_sum[i] = prefix_sum[i -1] + next_a
        prev_a = next_a
    return prefix_sum

if __name__ == '__main__':
    raw_input = sys.stdin.buffer.read().splitlines()
    result_exists = list()
    n, x, y, a0 = [int(_) for _ in raw_input[0].split()]
    m, z, t, b0 = [int(_) for _ in raw_input[1].split()]
    prefix_sum = count_prefix_sum(n, x, y, a0)
    m_size = 2 * m
    prev_b = b0
    c = [0] * m_size
    c[0] = b0 % n
    cum_sum = 0
    for i in range(1, m_size):
        next_b = (z * prev_b + t) % B_MOD
        c[i] = next_b % n
        prev_b = next_b
        if (i - 1) % 2 == 0:
            l = min(c[i - 1], c[i])
            r = max(c[i - 1], c[i])
            if l == 0:
                cum_sum += prefix_sum[r]
            else:
                cum_sum += prefix_sum[r] - prefix_sum[l - 1]
    print(cum_sum)


