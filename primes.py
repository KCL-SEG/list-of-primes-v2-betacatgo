"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
import math

def is_prime(num):
    if num == 2:
        return True
    elif num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError

    list = []
    num = 2
    while len(list) < number_of_primes:
        if is_prime(num):
            list.append(num)
        num += 1
    return list
