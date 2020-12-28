#!/usr/bin/env python3
""" linked list implementation """


class Node:
    """ One directional node """
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)


class LinkedList:
    """ Data structure """

    def __init__(self, val):
        self.head = Node(val)

    def __str__(self):
        result = ""
        tmp = self.head
        while tmp:
            result += str(tmp.val) + (' --> ' if tmp.next else '')
            tmp = tmp.next
        return result

    def append(self, val, after_node=None):
        """ add at element at the end or after specific node (by value) """
        tmp = self.head
        if not tmp:
            return

        while tmp.next and not(after_node is None and tmp.val == after_node):
            tmp = tmp.next

        another = tmp.next
        tmp.next = Node(val)
        tmp.next.next = another

    def prepend(self, val):
        """ add an alement at the begining """
        nd = Node(val)
        nd.next = self.head
        self.head = nd

    def remove(self, value):
        """ remove and element """
        nd = self.head
        if not nd:
            return

        if nd.val == value:
            self.head = nd.next

        while nd.next:
            if nd.next.val == value:
                nd.next = nd.next.next

            nd = nd.next


ts = LinkedList(6)
ts.append(10)
ts.append(21)
ts.append(12)
ts.append(33, 10)

ts.prepend(-1)

ts.remove(10)

print(ts)
