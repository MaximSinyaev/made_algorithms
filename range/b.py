"""

"""
import sys

SEPARATOR = "\n"
UNICODE = "utf-8"


def calculate_matrix(a, n):
    k = [1] * n
    matrix = [None for _ in range(n)]
    for i in range(1, n):
        k[i] = k[i - 1] if i + 1 <= k[i - 1] else k[i - 1] * 2

    for i in range(n):
        matrix[i] = [0] * k[i]
        for j in range(len(k[:n - i])):
            if j == 0:
                matrix[i][j] = a[i]
            else:
                matrix[i][j] = min(matrix[i][j - 1], matrix[i + k[j - 1]][j - 1])
    print(k)

if __name__ == '__main__':
    raw_input = sys.stdin.buffer.read().splitlines()
    result_exists = list()
    n, m, a0 = [int(_) for _ in raw_input[0].split()]
    u1, v1 = [int(_) for _ in raw_input[1].split()]
    a = [a0] * n
    for i in range(1, n):
        a[i] = (23 * a[i - 1] + 21563) % 16714589
    calculate_matrix(a, n)
    # response =
    # for i in range(m):
    #     u2 = ((17 * u1 + 751 + +2𝑖)mod𝑛)+1

    encoded_array = (SEPARATOR.join(result_exists)).encode(UNICODE)
    sys.stdout.buffer.write(encoded_array + '\n'.encode(UNICODE))
