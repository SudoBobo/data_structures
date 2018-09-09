
def is_anagram(str1, str2):

    if len(str1) != len(str2):
        return False

    sum1 = 0
    for l in str1:
        sum1 += ord(l)

    sum2 = 0
    for l in str2:
        sum2 += ord(l)

    return sum1 == sum2


def anagram_sort(a):
    head = 0
    a_size = len(a)
    while head < a_size:
        tail = head + 1
        for k in range(tail, a_size):
            if is_anagram(a[k], a[head]):
                a[k], a[tail] = a[tail], a[k]
                tail += 1
        head = tail


arr = ['abc', 'aabc', 'cab', 'bac', 'baca', 'aac']
exp = ['aac', 'aabc', 'baca', 'abc', 'bac', 'cab']

anagram_sort(arr)
print(arr)
print(exp)
