"""
WHAT
implement Stack

HOW
list.
"""

class Stack:
    """Stack()

    设定，把 list 末尾当作 stack 的 top 端。
    """
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self, item):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
