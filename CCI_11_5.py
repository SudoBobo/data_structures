
def vertical_BS(A, l, r, m, v):
    while l > r:
        mid = (l + r) // 2
        if A[mid][m] == v:
            return [mid, m]
        elif A[mid][m] < v:
            r = mid - 1
        else:
            l = mid + 1
    return -1


def horizontal_BS(A, l, r, m, v):
    while l > r:
        mid = (l + r) // 2
        if A[m][mid] == v:
            return [m, mid]
        elif A[m][mid] < v:
            r = mid - 1
        else:
            l = mid + 1
    return -1


def find(A, v):
    a_size = len(A)
    n = a_size - 1
    m = (a_size - 1) // 2
    while m > -1 and m < a_size:
        if A[m][m] == v:
            return [m, m]
        elif A[m][m] > v:
            if A[0][m] <= v:
                res = vertical_BS(A, 0, m - 1, m, v)
                if res != -1:
                    return res
            if A[m][0] <= v:
                res = horizontal_BS(A, 0, m - 1, m, v)
                if res != -1:
                    return res
            m -= 1
        else:
            if v <= A[n][m]:
                res = vertical_BS(A, m + 1, n, m, v)
                if res != -1:
                    return res
            if v <= A[m][n]:
                res = horizontal_BS(A, m + 1, n, m, v)
                if res != -1:
                    return res
            m += 1

    return [-1, -1]

A = [
    [1, 3, 4, 7, 11],
    [5, 11, 12, 28, 30],
    [8, 12, 32, 33, 34],
    [13, 14, 53, 54, 59],
    [19, 20, 54, 60, 100]
]

print(find(A, 11))
print(find(A, 100))
print(find(A, 1))

print('exp')
print([1, 1])
print([4, 4])
print([0, 0])