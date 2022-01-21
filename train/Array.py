# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#
from array import array


def twoArrays(k, A: array, B: array):
    hasPremunt = False
    for i in range(len(A)):
        hasPremunt = False
        for j in range(len(B)):
            if A[i] + B[j] >= k:
                hasPremunt = True
                continue
            if j == len(B) - 1 and hasPremunt != True:
                hasPremunt = False
                break
        else:
            continue
        break
    if hasPremunt:
        return "YES"
    else:
        return "NO"


# You match high values from one array with low values of the other array.
# The logic seems to be that if you can't match a low value with the next available high value,
# you won't be able to match it with any other value in the array,
# because all the other values available will be lower than the one you already got.
def twoArraysSolved(k, A, B):
    # Create two arrays (one sorted ascending, one sorted descending):
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        if A[i] + B[i] < k:
            return "NO"
    return "YES"


def twoArraysAdition(k, A, B):
    # Write your code here
    sortedA = sorted(A)
    sortedB = sorted(B, reverse=True)
    totalSum = (a + b for a, b in zip(sortedA, sortedB))

    if all((num >= k for num in totalSum)):
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    # print(twoArraysSolved(10, [6, 5, 4], [4, 5, 6])) #pass
    print(twoArraysSolved(10, [7, 6, 8, 4, 2], [5, 2, 6, 3, 1]))  # pass
    print(twoArraysAdition(10, [7, 6, 8, 4, 2], [5, 2, 6, 3, 1]))  # pass
    # print(twoArraysSolved(10, [2, 1, 3], [7, 8, 9])) #pass
    # print(twoArraysSolved(5, [1, 2, 2, 1], [3, 3, 3, 4]))
    # print(twoArraysSolved(5, [1, 2, 2, 1], [3, 3, 3, 4]))
