'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

'''

from utils.divisors import primes_sieve

def truncate_primes(limit=10**6):
    primes = set(primes_sieve(limit))
    memo = list()

    for prime in primes:

        prime_string = str(prime)
        front = prime_string
        back = prime_string
        if len(prime_string) < 2:
            continue

        for _ in range(len(prime_string)-1):
            back = back[:-1]
            front = front[1:]

            if int(back) not in primes or int(front) not in primes:
                break
        else:
           memo.append(prime)

    return memo

if __name__ == "__main__":
    answer = truncate_primes()
    print(len(answer))
    print(sum(answer))
