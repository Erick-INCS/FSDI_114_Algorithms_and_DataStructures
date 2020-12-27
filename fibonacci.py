#!/usr/bin/env python3
""" Fibonnacci """


def fibonacci(limit):
    """ fib """
    n0, n1 = 0, 1
    print(n0, n1, sep='\n')

    for _ in range(limit):
        n1, n0 = n1 + n0, n1
        print(n1)


fibonacci(10)
