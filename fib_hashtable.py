#!/usr/bin/env python3
from hash_table import HashTable

ht = HashTable(9999)

ht[0] = 0
ht[1] = 1

def hast_table_fibonacci(limit):
    """ fib with ht """
    
    if ht[limit] != None:
        return ht[limit]
    else:
        i = limit - 1
        while not ht[i]:
            i -= 1    

    for _ in range(i, limit):
        ht[i+1], ht[i] = ht[i] + ht[i-1], ht[i]
        i += 1

    return ht[i]


for i in range(100):
    print(hast_table_fibonacci(i))