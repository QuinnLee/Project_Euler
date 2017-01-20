'''
The prime 41, can be written as the sum of six consecutive primes:

  41 = 2 + 3 + 5 + 7 + 11 + 13
  This is the longest sum of consecutive primes that adds to a prime below one-hundred.

  The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

  Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''

from utils.divisors import primes_sieve, is_prime
from collections import defaultdict, Counter


if __name__ == "__main__":
    primes = primes_sieve()
    prime_set = set(primes)
    largest_prime_possible = 0

    prime_sums = [0]

    for p in primes:
        prime_sums.append(prime_sums[-1] + p)
        if prime_sums[-1] > 10**6:
            break

    count = 0

    for i in range(len(prime_sums)):
        for i_2 in range(len(prime_sums) - 1, i + count, -1):
            n = prime_sums[i_2] - prime_sums[i]

            if( i_2 - i > count and n in prime_set):
                count, max_prime = i_2 - i, n
                break

    print(count, max_prime)

