# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 13:12:20 2017

@author: mankayarkarasi.c
"""


# Read the List of values from Input, filter the Prime Numbers and output mean, median and mode values


def is_prime(item):

    """ is_prime function finds if the list given is prime number
    Args:
      item: an input values from the list
    Returns:
    True value if the number is prime or False value if the number is not prime
    """

    if item > 1:
        for i in range(2, item):
            if (item % i) == 0:
                return False
        else:
            return True
    else:
        return False


# Sort the Prime Number Values

def sorted_prime_number(items):

    """ sorted_prime_number function provides the sorted list of prime number value
    Args:
    items: an input values from the list
    Returns:
    sorted list of prime numbers in the given list
    """

    print(items)
    return [x for x in sorted(items)]


# Get the Median Value
def median(items):

    """
    gets the median value of the given list
    Args:
    items: an input values from the list
    Returns:
    median value of the given list
    """

    listlength = len(items)
    if (listlength % 2) == 0:
        return items[listlength/2] + items[(listlength/2) -1] / 2
    else:
        return items[listlength/2]


# Main Program to read the values, sort the prime numbers in the given list and
# then print mean, median, mode by grouping the list with 3 values.

def main():
    data = [x for x in input()]
    primes = sorted_prime_number(data)
    print(primes)
    result = [set(min(x), median(primes), max(x)) for x in primes]
    print(result)
