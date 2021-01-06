#!/usr/bin/env python3

from double_linked_list import DoubleLinkedList

def is_palindrome(inp):
    last = inp.head
    first = inp.head
    while last.next:
        last = last.next

    res = str(last) == str(first)
    while res and last and first:
        first = first.next
        last = last.prev
        res &= str(last) == str(first)
        
    return res


dll = DoubleLinkedList('b')
for i in 'ob':
    dll.append(i)

print('"bob" is palindrome?', is_palindrome(dll))