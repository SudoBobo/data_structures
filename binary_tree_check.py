from collections import deque
import sys

sys.setrecursionlimit(100000)


class Node:
    def __init__(self, key, l_idx, r_idx):
        self.key = key
        self.l_idx = l_idx
        self.r_idx = r_idx


def check_1(root, arr, must_be_bigger_then, must_be_lesser_then):
    if root.l_idx > -1 and not root.key > arr[root.l_idx].key:
        return False
    if root.r_idx > -1 and not root.key < arr[root.r_idx].key:
        return False
    if must_be_bigger_then is not None:
        if not root.key > must_be_bigger_then:
            return False
    if must_be_lesser_then is not None:
        if not root.key < must_be_lesser_then:
            return False
    left_res = True
    right_res = True
    if root.l_idx > -1:
        left_res = check_1(arr[root.l_idx], arr, must_be_bigger_then, root.key)
    if root.r_idx > -1:
        right_res = check_1(arr[root.r_idx], arr, root.key, must_be_lesser_then)
    return left_res and right_res


n = int(input())
arr = []
for _ in range(0, n):
    temp = [int(number) for number in input().split(' ')]
    arr.append(Node(temp[0], temp[1], temp[2]))

if len(arr) == 0:
    print('CORRECT')
else:
    is_ok = check_1(arr[0], arr, None, None)
    if is_ok:
        print('CORRECT')
    else:
        print('INCORRECT')
