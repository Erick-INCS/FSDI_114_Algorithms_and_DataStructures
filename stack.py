#!/usr/bin/env python
""" Stack """


class Stack():
    """ Stack implementation """
    def __init__(self):
        self.items = []

    def is_empty(self):
        """ returns true if the inner list is empty """
        return self.items == []

    def push(self, items):
        """ push ... """
        self.items.append(items)

    def pop(self):
        """ pop ... """
        return self.items.pop()

    def peek(self):
        """ peek ... """
        return self.items[len(self.items) - 1]

    def size(self):
        """ returns the inner array size """
        return len(self.items)


def implement():
    """ Implementation """

    s_k = Stack()
    some_str = "Hello ..."
    result_str = ""

    for i in some_str:
        s_k.push(i)

    while not s_k.is_empty():
        result_str += s_k.pop()

    print(f"'{some_str}' -> '{result_str}'")


if __name__ == "__main__":
    implement()

# homework palindrome?
