class MinHeap:
    def __init__(self, arr, arr_size):
        self.arr_size = arr_size
        self.arr = arr

        self.swap_counter = 0
        self.swap_log = []

        for i in range(arr_size // 2, -1, -1):
            self.sift_down(i)

    def sift_down(self, i):
        # idx of minimum element between arr[i], it's left and right children
        i_min = i

        l_idx = self.left_child(i)
        if l_idx < self.arr_size and self.arr[l_idx] < self.arr[i_min]:
            i_min = l_idx

        r_idx = self.right_child(i)
        if r_idx < self.arr_size and self.arr[r_idx] < self.arr[i_min]:
            i_min = r_idx

        if i_min != i:
            self.swap(i, i_min)
            self.sift_down(i_min)

    def extract_min(self):
        min = self.arr[0]

        self.arr[0] = self.arr[self.arr_size - 1]
        self.arr_size -= 1

        self.sift_down(0)

        return min

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        self.swap_counter += 1
        self.swap_log.append([i, j])


arr_size = int(input())
arr = [int(number) for number in input().split(' ')]

min_heap = MinHeap(arr, arr_size)

print(min_heap.swap_counter)
for swap in min_heap.swap_log:
    print(*swap)