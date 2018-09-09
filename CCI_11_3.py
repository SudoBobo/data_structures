
def find(A, v):
    l = 0
    r = len(A) - 1

    while l < r:
        mid = (l + r) // 2

        if A[mid] == v:
            return mid
        elif A[mid] < v and v <= A[r]:
            l = A[mid] + 1
        elif A[l] <= v and v < A[mid]:

A = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
B = []
print('exp', 8)
print('res', find(A, 5))