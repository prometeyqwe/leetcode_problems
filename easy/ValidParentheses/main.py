"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""


class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        return self.stack_list.pop(-1) if len(self.stack_list) else ''

    def __len__(self):
        return len(self.stack_list)


class Solution:
    def __init__(self):
        self.types = set(['()', '{}', '[]'])
        self.close_brackets = (')', '}', ']')
        self.stack = Stack()

    def isValid(self, s):
        for i in s:
            if i in self.close_brackets:
                if ''.join((self.stack.pop(), i)) in self.types:
                    continue
                else:
                    return False
            else:
                self.stack.push(i)
        return True if not len(self.stack) else False


if __name__ == '__main__':
    s1 = Solution()
    print('result: {}'.format(s1.isValid(']')))
