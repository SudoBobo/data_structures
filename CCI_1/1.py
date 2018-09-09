

# solution expecting ASCII 'a-z' string and requires only one byte of additional space
def is_all_unique(s):
    checker = 0
    for i in range(len(s)):
        val = ord(s[i]) - ord('a')
        if (checker & (1 << val)) > 0:
            return False
        checker |= 1 << val
    return True



inputs = [
    'aaa',
    'abca',
    'abcde',
    'abcdef'
]

results = [
    False,
    False,
    True,
    True,
]

for i in range(len(inputs)):
    print(inputs[i], results[i], is_all_unique(inputs[i]))
