'''
The first two consecutive numbers to have two distinct prime factors are:

  14 = 2 × 7
  15 = 3 × 5

  The first three consecutive numbers to have three distinct prime factors are:

    644 = 2² × 7 × 23
    645 = 3 × 5 × 43
    646 = 2 × 17 × 19.

    Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
'''

from utils.divisors import primes_sieve, prime_factors
from collections import Counter

def consecutive_primes(count=2):

  memo = list()
  primes = set(primes_sieve())
  uniq_primes = list()

  for n in range(0, 10**6):
      if len(memo) == count:
          return memo

      factors = Counter(prime_factors(n))

      if len(set(factors)) == count and factors not in uniq_primes:
          memo.append(n)
          uniq_primes.append(factors)
      else:
          memo = list()
          uniq_primes = [factors]



if __name__ == "__main__":
    print(3)
    print(consecutive_primes(3))
    print(4)
    print(consecutive_primes(4))
