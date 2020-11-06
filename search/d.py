"""
С утра шел дождь, и ничего не предвещало беды. Но к обеду выглянуло солнце, и в лагерь заглянула СЭС. Пройдя по всем
домикам и корпусам, СЭС вынесла следующий вердикт: бельевые веревки в жилых домиках не удовлетворяют нормам СЭС. Как
выяснилось, в каждом домике должно быть ровно по одной бельевой веревке, и все веревки должны иметь одинаковую длину.
В лагере имеется N бельевых веревок и K домиков. Чтобы лагерь не закрыли, требуется так нарезать данные веревки, чтобы
среди получившихся веревочек было K одинаковой длины. Размер штрафа обратно пропорционален длине бельевых веревок,
которые будут развешены в домиках. Поэтому начальство лагеря стремиться максимизировать длину этих веревочек.

Входные данные
В первой строке заданы два числа — N и K (1 ≤ N, K ≤ 10001). Далее в каждой из последующих N строк
записано по одному числу — длине очередной бельевой веревки. Длина веревки задана в сантиметрах. Все длины лежат в
интервале от 1 сантиметра до 100 километров включительно.

Выходные данные
В выходной файл следует вывести одно целое число — максимальную длину веревочек, удовлетворяющую условию, в сантиметрах.
В случае, если лагерь закроют, выведите 0.
"""
import sys

def check_lines_number(ar, length):
    return sum([line // length for line in ar])

def bin_search(ar, k):
    l = 0
    r = ar[-1] + 1
    while l < r - 1:
        m = (l + r) // 2
        if check_lines_number(ar, m) >= k:
            l = m
        else:
            r = m
    return r


if __name__ == '__main__':
    raw_input = sys.stdin.read().splitlines()
    n, k = [int(_) for _ in raw_input[0].split()]
    ar = [0] * n
    for i in range(n):
        ar[i] = int(raw_input[1 + i])
    ar.sort()
    ans = bin_search(ar, k)
    print(ans - 1 if ans != 0 else 0)
