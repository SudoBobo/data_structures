
class bracket():
    def __init__(self, char, position):
        self.char = char
        self.position = position

def match(left_br, right_br):

    if left_br == '(' and right_br == ')':
        return True

    if left_br == '[' and right_br == ']':
        return True

    if left_br == '{' and right_br == '}':
        return True

    return False

def is_balanced(line):
    stack = list()
    brackets = {'(', '[', '{'}
    closing_brackets = {')', ']', '}'}

    current_element_number = 1
    first_open_without_close = 1

    for char in line:
        if char in brackets:
            stack.append(bracket(char, current_element_number))

        elif char in closing_brackets:

            if len(stack) == 0:
                return current_element_number

            top = stack.pop()

            if not match(top.char, char):
                return current_element_number

        current_element_number += 1

    if len(stack) != 0:
        return stack[0].position

    return 'Success'


line = input()

print(is_balanced(line))