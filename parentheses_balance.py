#!/usr/bin/env python3
""" Check Parentheses Balance """
from stack import Stack

data = ['(({[({}){}]}[])[])',    # True
        '{({[{[(({[]}))]}]})}',  # True
        '[[[[[}{{(())}}]]]]]',   # False
        '{{(()))}}{{}}()',       # False
        '()[]{}{}{{}}(())[[]]']  # True


def is_balanced(phs, c_map={'}': '{', ']': '[', ')': '('}):
    """ Check if given string of parentheses is balanced """
    sk_ = Stack()

    for ch_ in phs:
        if ch_ not in c_map.keys():
            sk_.push(ch_)

        elif sk_.pop() != c_map[ch_]:
            return False

    return True


print("\nValidation.\n\tExpected: T, T, F, F, T\n")
for i in data:
    print(is_balanced(i))
