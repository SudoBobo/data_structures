from array import array

def window_max(arr, array_size, window_size):
    maximums = list()

    # check dumb cases

    elems_q =  array('I', window_size)
    max_q = arr('I', window_size)

    # init
    first_max = -1
    for i in range(window_size):
        elems_q[window_size - 1 - i] = arr[i]
        first_max = max(first_max, arr[i])

    for i in range(window_size):
        max_q[i] = first_max

    # work
    for j in range(window_size, n):
        pass
array_size = int(input())
arr = [int(number) for number in input().split(' ')]
window_size = int(input())

print(*window_max(arr, array_size, window_size))