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


s = Stack()

number_of_commands = int(input())
for i in range(number_of_commands):
    line = input().split(' ')

    command = line[0]

    if command == 'max':
        print(s.get_max())

    if command == 'pop':
        s.pop()

    if command == 'push':
        s.push(int(line[1]))
