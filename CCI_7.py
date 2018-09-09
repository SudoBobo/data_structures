
def can_continue(S, i, j):
    return S[i][0] > S[j][0] and S[i][1] > S[j][0]

mem = dict()
def max_length_of_subseq_which_ends_here(S, i):
    if i == 0:
        return 1
    if i in mem:
        return mem[i]
    else:
        max = 1
        for j in range(0, i):
            if can_continue(S, i, j):
                res = max_length_of_subseq_which_ends_here(S, j) + 1
                if res > max:
                    max = res
        mem[i] = max

    return mem[i]

S = [[]]

def find_max_tower_length(S):
    S.sort(key=lambda item: item[0])
    S.sort(key=lambda item: item[1])

    res = 0
    for i in range(0, len(S)):
           res = max_length_of_subseq_which_ends_here(S, i)
    return res