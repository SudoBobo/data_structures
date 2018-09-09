from collections import deque


class Key:
    def __init__(self, key):
        self.key = key


class Node:
    def __init__(self, key, l_idx, r_idx):
        self.key = key
        self.l_idx = l_idx
        self.r_idx = r_idx


def in_order(root, arr):
    q = deque()
    res_str = ''
    q.append(root)
    while len(q) > 0:
        elem = q.pop()
        if isinstance(elem, Key):
            res_str += str(elem.key)
            res_str += ' '
        else:
            if elem.r_idx > -1:
                q.append(arr[elem.r_idx])
            q.append(elem.key)
            if elem.l_idx > -1:
                q.append(arr[elem.l_idx])
    return res_str


def pre_order(root, arr):
    q = deque()
    res_str = ''
    q.append(root)
    while len(q) > 0:
        elem = q.pop()
        if isinstance(elem, Key):
            res_str += str(elem.key)
            res_str += ' '
        else:
            if elem.r_idx > -1:
                q.append(arr[elem.r_idx])
            if elem.l_idx > -1:
                q.append(arr[elem.l_idx])
            q.append(elem.key)

    return res_str


def post_order(root, arr):
    q = deque()
    res_str = ''
    q.append(root)
    while len(q) > 0:
        elem = q.pop()
        if isinstance(elem, Key):
            res_str += str(elem.key)
            res_str += ' '
        else:
            q.append(elem.key)
            if elem.r_idx > -1:
                q.append(arr[elem.r_idx])
            if elem.l_idx > -1:
                q.append(arr[elem.l_idx])

    return res_str


n = int(input())
arr = []
for _ in range(0, n):
    line = [int(number) for number in input().split(' ')]
    arr.append(Node(Key(line[0]), line[1], line[2]))
root = arr[0]
print(in_order(root, arr))
print(pre_order(root, arr))
print(post_order(root, arr))
