"""
Пусть a1,a2,...,an — числовая последовательность. Длина последовательности — это количество элементов этой 
последовательности. Последовательность ai1,ai2,...,aik называется подпоследовательностью последовательности a, если 1≤
i1 < i2 < ... < ik ≤ n. Последовательность a называется возрастающей, если a1 < a2 < ... < an.
Вам дана последовательность, содержащая n целых чисел. Найдите ее самую длинную возрастающую подпоследовательность.

Входные данные
В первой строке задано одно число n (1 ≤ n ≤ 2000) — длина подпоследовательности. В следующей строке задано n целых
чисел ai ( -109 ≤ ai ≤ 109) — элементы последовательности.

Выходные данные

В первой строке выведите число k — длину наибольшей возрастающей подпоследовательности. В следующей строке выведите k
чисел — саму подпоследовательность.
"""
import sys


def find_biggest_subsequence(n, ar):
    fp = [1] * n
    pred = [-1] * n
    max_fp = 1
    max_pos = n - 1
    for i in range(1, n):
        for j in range(i):
            if ar[i] > ar[j]:
                if fp[j] + 1 > fp[i]:
                    fp[i] = fp[j] + 1
                    pred[i] = j
                if fp[i] > max_fp:
                    max_fp = fp[i]
                    max_pos = i
                    # break
    subseq = list()
    while 1:
        subseq.append(ar[max_pos])
        max_pos = pred[max_pos]
        if max_pos == -1:
            break
    return max_fp, subseq[::-1]


if __name__ == '__main__':
    raw_input = sys.stdin.buffer.read().splitlines()
    result_exists = list()
    n = int(raw_input[0])
    ar = [int(_) for _ in raw_input[1].split()]
    max_len, subseq = find_biggest_subsequence(n, ar)
    print(max_len)
    print(*subseq)
