#!/usr/bin/env python3
""" Coding challenges! """

""" 1.- Given a string, write a function that uses recursion to reverse it. """
def reverse(s, rs=""):
    if s == "":
        return rs
    else:
        return reverse(s[:-1], rs + s[-1])

print(f'1.- "sample string" => {reverse("sample string")}')


""" 2.- Given a list of integers, write a function that will return a list, in which for each index the element will be the product of all the integers except for the element at that index. """
def mult_map(ls):
    org = ls.copy()

    def mult(l):
        r = 1
        for i in l:
            r *= i
        return r

    for i in range(len(ls)):
        arr = org[:i] + org[i + 1:]
        ls[i] = mult(arr)

a = [1,3,5,4,2]
print(f"2.- {a} -> ", end="")
mult_map(a)
print(a)
