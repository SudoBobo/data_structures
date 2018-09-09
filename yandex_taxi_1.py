
N, R = [int(number) for number in input().split(' ')]
arr = [int(number) for number in input().split(' ')]

arr = sorted(arr)
res = 0
# todo make version that will not change original array
# make an assumption that all coordinates are positive
while len(arr) > 0:
    leftest = arr[0]
    r = 0
    if len(arr) == 0:
        res += 1
        arr = arr[1:]
        print('exiting ' + str(leftest))
        break

    while r + 1 < len(arr) and leftest + R >= arr[r + 1]:
        r += 1

    if r == 0:
        res += 1
        arr = arr[1:]
        print('can not reach any ' + str(leftest))
        continue

    after_r = r
    while after_r + 1 < len(arr) and arr[after_r + 1] <= arr[r] + R:
        after_r += 1

    res += 1

    arr = arr[after_r + 1:]

print(res)
