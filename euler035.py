'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

'''

from itertools import permutations
from utils.divisors import is_prime
from collections import deque

def circular_prime(limit=10**6):
    memo = set()
    non_circular_primes = set()
    for number in range(2, limit +1):
        if not is_prime(number):
            continue

        number_d = deque(str(number))
        p_list = list()

        for rotation in range(len(number_d)):
            number_d.rotate(1)
            if not is_prime(int("".join(number_d))):
                  break
        else:
            memo.add(number)


    return memo

if __name__ == "__main__":
    print(len(circular_prime(100)))
    print(len(circular_prime()))

