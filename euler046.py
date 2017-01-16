'''
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''

from utils.divisors import primes_sieve

def composite(limit=10**3):
    numbers = set([ _ for _ in range(1,limit) if _ % 2 == 1])

    primes = set(primes_sieve(limit))

    for _ in range(0, limit):
        for p in primes:
            n = int(p + 2*_**2)
            if n in numbers:
                numbers.remove(n)

    return numbers

if __name__ == "__main__":
    print(composite(10**4))
