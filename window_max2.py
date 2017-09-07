from array import array


class Stack:
    def __init__(self):
        self.top = -1
        self.arr = array('I')
        self.max = array('I')

    def push(self, elem):
        self.top += 1
        self.arr.append(elem)

        if self.top > 0:
            self.max.append(max(elem, self.max[self.top - 1]))
        else:
            self.max.append(elem)

    def pop(self):
        self.top -= 1
        self.max.pop()
        return self.arr.pop()

    def get_max(self):
        return self.max[self.top]

    def empty(self):
        return self.top == -1


class MaxDeque:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def push_back(self, number):
        self.in_stack.push(number)

    def return_curr_max(self):

        if self.out_stack.empty():
            while not self.in_stack.empty():
                self.out_stack.push(self.in_stack.pop())

        if self.in_stack.empty():
            return self.out_stack.get_max()
        else:
            return max(self.in_stack.get_max(), self.out_stack.get_max())

    def pop(self):
        return self.out_stack.pop()


array_size = int(input())
arr = [int(number) for number in input().split(' ')]
window_size = int(input())

d = MaxDeque()
for i in range(window_size):
    d.push_back(arr[i])

output = list()
for j in range(window_size, array_size):
    output.append(d.return_curr_max())
    d.pop()
    d.push_back(arr[j])

output.append(d.return_curr_max())
print(*output)
