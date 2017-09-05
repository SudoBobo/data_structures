
class Buffer:
    def __init__(self, size):
        self.__size = size
        # store the time for the completion of package processing
        self.__buffer = []
        self.__last_elem_idx = -1
        self.proc_start_times = []

    def drop_proceeded(self, arrival_time):
        while not self.empty() and self.__buffer[0] <= arrival_time:
            self.__buffer.pop(0)
            self.__last_elem_idx -= 1

    def add(self, arrival_time, duration):

        self.drop_proceeded(arrival_time)

        if self.empty():
            self.proc_start_times.append(arrival_time)
            self.__buffer.append(arrival_time + duration)
            self.__last_elem_idx += 1
            return

        if not self.full():
            proc_start_time = self.__buffer[self.__last_elem_idx]
            self.proc_start_times.append(proc_start_time)
            self.__buffer.append(proc_start_time + duration)
            self.__last_elem_idx += 1
            return

        if self.full():
            self.proc_start_times.append(-1)
            return

    def empty(self):
        return self.__last_elem_idx == -1

    def full(self):
        return self.__last_elem_idx == (self.__size - 1)

size, n = map(int, input().split(' '))
arrivals = []
durations = []

if n > 0:
    for i in range(n):
        line = input().split(' ')
        arrivals.append(int(line[0]))
        durations.append(int(line[1]))

    buffer = Buffer(size)

    for i in range(n):
        buffer.add(arrivals[i], durations[i])

    for time in buffer.proc_start_times:
        print(time)

else:
    print('')

