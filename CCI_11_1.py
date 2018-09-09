
def merge_sort_into_A(A, B):
    a_size = len(A)
    b_size = len(B)

    # a = 0
    b = 0
    buffer_l = a_size - b_size
    assert (A[buffer_l] == 'none')
    buffer_r = buffer_l

    for a in range(0, a_size - b_size):
        # TODO handle right case

        if b < b_size and buffer_r < a_size:

            if A[buffer_l] == 'none':
                if A[a] <= B[b]:
                    pass
                else:
                    assert (A[buffer_r] == 'none')
                    A[buffer_r] = A[a]
                    buffer_r += 1
                    A[a] = B[b]
                    b += 1

            if A[buffer_l] != 'none':
                if B[b] <= A[buffer_l]:
                    assert (A[buffer_r] == 'none')
                    A[buffer_r] = A[a]
                    buffer_r += 1
                    A[a] = B[b]
                    b += 1
                else:
                    assert (A[buffer_r] == 'none')
                    A[buffer_r] = A[a]
                    buffer_r += 1
                    assert (A[buffer_l] != 'none')
                    A[a] = A[buffer_l]
                    A[buffer_l] = 'none'
                    buffer_l += 1

        if b == b_size:
            assert (A[buffer_r] == 'none')
            A[buffer_r] = A[a]
            buffer_r += 1
            assert (A[buffer_l] != 'none')
            A[a] = A[buffer_l]
            A[buffer_l] = 'none'
            buffer_l += 1

    print(A)
    for a in range(a_size - b_size, a_size):
        if buffer_l == buffer_r or A[buffer_l] == 'none':
            A[a] = B[b]
            b += 1
        if b == b_size:
            A[a] = A[buffer_l]
            buffer_l += 1
        if buffer_l < buffer_r and A[buffer_l] <= B[b]:
            A[a] = A[buffer_l]
            buffer_l += 1
        else:
            A[a] = B[b]
            b += 1

A = [1, 3, 6, 7, 'none', 'none', 'none' ]
B = [2, 4, 9]

merge_sort_into_A(A, B)
print(A)
print([1,2,3,4,6,7,9])