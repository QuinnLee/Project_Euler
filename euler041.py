'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

'''

from utils.divisors import primes_sieve, is_prime
from collections import Counter

def pandigital_primes(primes):
    memo = list()

    print('starting')

    for prime in primes:
        counter = Counter(str(prime))
        v = Counter([str(_) for _ in range(1, len(str(prime))+1)])
        if counter == v:
            memo.append(prime)

    return memo


if __name__ == "__main__":
    answer = pandigital_primes(primes_sieve(10**7))
    print(answer[-1])
