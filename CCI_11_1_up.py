

def merge_sort_into_A(A, B):
    a_size = len(A)
    b_size = len(B)

    a = a_size - b_size - 1
    b = b_size - 1

    i = a_size - 1
    while A[i] == 'none':
        if b > -1 and a > -1:
            if A[a] > B[b]:
                A[i] = A[a]
                A[a] = 'none'
                a -= 1
            else:
                A[i] = B[b]
                b -= 1
        elif b > - 1:
            A[i] = B[b]
            b -= 1
        elif a > -1:
            pass

        i -= 1



A = [1, 3, 6, 7, 'none', 'none', 'none']
B = [2, 4, 9]

AA = [10, 'none', 'none', 'none']
BB = [2, 4, 11]
merge_sort_into_A(AA, BB)
print(AA)