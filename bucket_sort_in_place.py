
def get_bin(int):
    res = bin(int)
    return res[2:]


def get_pos(i, pos):

    b = get_bin(i)

    if len(b) > pos:
        return b[pos]
    else:
        return 0


def in_place_radix_sort(A, max_pos):
    for pos in range(0, max_pos + 1):
        l = 0
        r = len(A) - 1
        print('pos', pos)

        while l < r:
            print("l, r", l, r)
            print(get_pos(A[l], pos), get_pos(A[r], pos))
            if get_pos(A[l], pos) == 1:
                if get_pos(A[r], pos) == 0:
                    A[l], A[r] = A[r], A[l]
                    r -= 1
                    l += 1
                else:
                    r -= 1
            else:
                l += 1


A = [123, 321, 666, 0, 1, 2, 10000, 6617]
exp = sorted(A)
in_place_radix_sort(A, 4)
print(exp)
print(A)