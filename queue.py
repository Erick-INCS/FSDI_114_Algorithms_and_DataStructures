#!/usr/bin/env python
# -*- coding: utf8 -*-
""" Queue implementation """


class Queue:
    """ The """
    def __init__(self):
        self.items = []

    def is_empty(self):
        """ linter """
        return self.items == []

    def enqueue(self, item):
        """ is """
        self.items.insert(0, item)

    def dequeue(self):
        """ very """
        return self.items.pop()

    def size(self):
        """ annoying """
        return len(self.items)
