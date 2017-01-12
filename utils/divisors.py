from math import sqrt

def divisors(number):
    divisors = set([1.0])
    half_way_point = int(sqrt(number)) +1
    for n in range(1, half_way_point):
        divisor = number / n
        if divisor.is_integer() and divisor != number:
            divisors.add(n)
            divisors.add(divisor)

    return divisors

def is_prime(number):
    return len(divisors(number)) == 1

def primes_sieve(limit=10**6):
    not_prime = set()
    primes = []

    for i in range(2, limit+1):
        if i in not_prime:
            continue

        for f in range(i*2, limit+1, i):
            not_prime.add(f)

        primes.append(i)

    return primes

