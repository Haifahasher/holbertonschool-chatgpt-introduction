#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if len(sys.argv) < 2:
    print("Error: Please provide a number as an argument.")
else:
    f = factorial(int(sys.argv[1]))
    print(f)