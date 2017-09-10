class PhoneTableDirectAddressing:
    def __init__(self, max_size_of_number):
        self.names = [-1 for number in range(10 ** max_size_of_number + 1)]

    def add(self, number, name):
        self.names[number] = name

    def delete(self, number):
        self.names[number] = -1

    def find(self, number):
        if self.names[number] == -1:
            return 'not found'
        else:
            return self.names[number]


number_max_size = 7
table = PhoneTableDirectAddressing(number_max_size)

number_of_requests = int(input())
requests_results = []

for request in range(number_of_requests):
    command = input().split(' ')

    if command[0] == 'find':
        requests_results.append(table.find(int(command[1])))
    if command[0] == 'del':
        table.delete(int(command[1]))
    if command[0] == 'add':
        number = int(command[1])
        name = command[2]
        table.add(number, name)

for request_result in requests_results:
    print(request_result)