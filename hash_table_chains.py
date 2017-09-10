class HashTable:
    def __init__(self, table_size, p, x):
        self.table = [[] for table in range(table_size)]
        # denoted in the lecture
        self.p = p
        self.x = x
        self.m = table_size

    def add(self, string):
        string_hash = self.get_hash(string)

        chain_string_idx = self.find(string, string_hash)

        if chain_string_idx == -1:
            self.table[string_hash - 1].insert(0, string)

    def check(self, i):
        if len(self.table[i - 1]) == 0:
            return ''
        else:
            return self.table[i - 1]

    def delete(self, string):
        # find chain of determine that there is no such string at all
        string_hash = self.get_hash(string)
        chain_string_idx = self.find(string, string_hash)
        if chain_string_idx == -1:
            pass
        else:
            del self.table[string_hash - 1][chain_string_idx]

    # returns index of first occurrence of 'string' in chain
    def find(self, string, string_hash=-1):
        if string_hash == -1:
            string_hash = self.get_hash(string)

        assert (string_hash > -1)

        for chain_string_idx in range(len(self.table[string_hash - 1])):
            if string == self.table[string_hash - 1][chain_string_idx]:
                return chain_string_idx
        return -1

    def get_hash(self, string):
        ascii_repr = [ord(char) for char in string]
        result_hash = 0
        for i in range(len(ascii_repr)):
            result_hash += ((ascii_repr[i] * ((self.x ** i))))
        result_hash = result_hash % self.p
        result_hash = result_hash % self.m
        return result_hash


table_size = int(input())
p = 1000000007
x = 263
hash_table = HashTable(table_size, p, x)

number_of_requests = int(input())
requests_results = []

for request in range(number_of_requests):
    command = input().split(' ')

    if command[0] == 'add':
        hash_table.add(command[1])

    elif command[0] == 'check':
        res = hash_table.check(int(command[1]))
        if res == '':
            print('')
        else:
            print(*res)

    elif command[0] == 'del':
        hash_table.delete(command[1])

    elif command[0] == 'find':
        res = hash_table.find(command[1])
        if res == -1:
            print('no')
        else:
            print('yes')
