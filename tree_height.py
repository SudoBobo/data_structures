
import sys
sys.setrecursionlimit(20000)

def height(elem_number):

    if heights[elem_number] != -1:
        return heights[elem_number]
    else:
        h = 1
        for child_number in children[elem_number]:
            h = max(h, 1 + height(child_number))

        heights[elem_number] = h
        return h

def height_BU(parents, n):

    height_from_element_to_root = [-1 for i in range(n)]

    for elem_number in range(n):
        parent_number = parents[elem_number]

        height_from_current_element_to_root = 1
        while parent_number != -1:

            if height_from_element_to_root[parent_number] == -1:
                height_from_current_element_to_root += 1
                parent_number = parents[parent_number]
            else:
                height_from_current_element_to_root += height_from_element_to_root[parent_number]
                break

        height_from_element_to_root[elem_number] = height_from_current_element_to_root

    return max(height_from_element_to_root)


n = int(input())

line = input()

parents = [int(i) for i in line.split(' ')]
children = [[] for i in range(n)]

root = 1000

for p in range(n):
    parent = parents[p]
    if parent != -1:
        children[parent].append(p)
    else:
        root = p

# height[elem_number] = tree highness in at this point
heights = [-1 for i in range(n)]
print(height_BU(parents, n))