#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
    This function computes the factorial of a given non-negative integer n
    recursively. The factorial of a number n (denoted as n!) is the product
    of all positive integers less than or equal to n.

    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the input number n.
    If n is 0, the function returns 1 as 0! = 1 by definition.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Parse the input number from the command line
f = factorial(int(sys.argv[1]))

# Print the result
print(f)
