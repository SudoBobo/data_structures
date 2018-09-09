
def gt(s1, s2):
    s2_size = len(s2)
    for l1 in range(0, len(s1)):
        if l1 == s2_size:
            return True
        if s1[l1] > s2[l1]:
            return True
        if s1[l1] < s2[l1]:
            return False
        if s1[l1] == s1[l1]:
            pass
    return False


def find(strings, v):
    if len(strings) == 0 or v == '':
        return -1

    l = 0
    r = len(strings) - 1

    while l < r:
        mid = (l + r) // 2
        if strings[mid] == '':
            mid_l = mid - 1
            mid_r = mid + 1

            while l <= mid_l and mid_r <= r:
                if strings[mid_l] != '':
                    mid = mid_l
                    break
                if strings[mid_r] != '':
                    mid = mid_r
                    break

                mid_l -= 1
                mid_r += 1

        if strings[mid] == '':
            return -1

        if strings[mid] == v:
            return mid
        elif gt(strings[mid], v):
            r = mid - 1
        else:
            l = mid + 1

    return -1


strings = ['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '']
print(find(strings, 'ball'))
print(find(strings, 'at'))
print(find(strings, 'car'))
print(find(strings, 'dad'))

print('right answers')
print(strings.index('ball'))
print(strings.index('at'))
print(strings.index('car'))
print(strings.index('dad'))
