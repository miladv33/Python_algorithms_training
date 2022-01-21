# wrong
from array import array


def firstBirthday(s, d, m):
    result = 0
    temp = 0
    added = 0
    for i in range(len(s)):
        if added == d:
            added = 0
            if temp == m:
                result += 1
        else:
            temp += s[i]
            added += 1
    return result


def Birthday(s: array, d, m):
    print(sum(s))


if __name__ == '__main__':
    # print(firstBirthday([1, 2, 1, 3, 2], 2, 3))
    Birthday([1, 2, 1, 3, 2], 2, 3)
