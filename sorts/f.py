"""
Задача F

Через сортировку слиянием
"""
rome_digits = {
    'I': 1,
    'II': 2,
    'III': 3,
    'V': 5,
    'IV': 4,
    'VI': 6,
    'VII': 7,
    'VIII': 8,
    'IX': 9,
    'L': 50,
    'XL': 40
}


def compare_kings(king1, king2):
    if king1[0] < king2[0]:
        return 1
    elif king1[0] == king2[0]:
        if king1[2] < king2[2]:
            return 1
        else:
            return 0
    else:
        return 0


def merge(left, right):
    left_len = len(left)
    right_len = len(right)
    i = 0
    j = 0
    res = [0] * (left_len + right_len)
    while (i + j) < (left_len + right_len):
        if i < left_len and j < right_len and compare_kings(left[i], right[j]):
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
    kings = list()
    for _ in range(n):
        name, rome_num = input().strip().split()
        king = [name, rome_num, 0]
        temp = king[1]
        for digit in list(rome_digits.keys())[::-1]:
            idx = temp.find(digit)
            if idx != -1:
                king[2] += rome_digits[digit]
                temp = temp[:idx] + temp[idx + len(digit):]
                if len(temp) == 0:
                    break
        king[2] += temp.count('X') * 10
        kings.append(king)
    for i, king in enumerate(merge_sort(kings)):
        print(*king[:2])
