"""
Project Euler #1: Multiples of 3 and 5

https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem
"""
#!/bin/python3

import sys

def sum(n, k):
    d = n // k
    return k * (d * (d+1)) // 2

def euler1(n):
    return sum(n, 3) + sum(n, 5) - sum(n, 15)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(euler1(n-1))
