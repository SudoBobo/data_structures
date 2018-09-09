
def get_key(str):
    sum = 0
    for l in str:
        sum += ord(l)
    return sum


def anagram_sort(a):
    hash_table = dict()

    for s in a:
        key = get_key(s)
        if key in hash_table:
            hash_table[key].append(s)
        else:
            hash_table[key] = [s, ]

    print(hash_table)
    i = 0
    for elem in hash_table:
        for e in hash_table[elem]:
            a[i] = e
            i += 1

arr = ['abc', 'aabc', 'cab', 'bac', 'baca', 'aac']
exp = ['aac', 'aabc', 'baca', 'abc', 'bac', 'cab']

anagram_sort(arr)
print(arr)
print(exp)