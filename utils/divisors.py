from math import sqrt

def divisors(number):
    divisors = set([1])
    half_way_point = int(sqrt(number)) +1
    for n in range(1, half_way_point):
        divisor = number / n
        if divisor.is_integer() and divisor != number:
            divisors.add(int(n))
            divisors.add(int(divisor))

    return divisors

def prime_factors(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

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

