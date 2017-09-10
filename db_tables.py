import sys

sys.setrecursionlimit(20000)

class Table:
    def __init__(self, size):
        self.size = size
        self.symlink = self


def union(destination, source, max_size):
    destination = find_real_tablePC(destination)
    source = find_real_tablePC(source)

    if destination is not source:
        destination.size += source.size
        source.size = 0
        source.symlink = destination
        max_size = max(max_size, destination.size)

    return max_size

def find_real_tablePC(table):
    if table is not table.symlink:
        table.symlink = find_real_tablePC(table.symlink)
    return table.symlink


number_of_tables, number_of_requests = map(int, input().split(' '))
tables_sizes = [int(table_size) for table_size in input().split(' ')]
max_size = max(tables_sizes)

tables = [Table(table_size) for table_size in tables_sizes]

maxs = []
for request in range(number_of_requests):
    destination, source = map(int, input().split(' '))
    max_size = union(tables[destination - 1], tables[source - 1], max_size)
    maxs.append(max_size)

for max in maxs:
    print(max)