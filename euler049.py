'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''

from utils.divisors import primes_sieve, is_prime
from collections import defaultdict, Counter

def same_permutation(a, b):
    d = defaultdict(int)
    for x in a:
        d[x] += 1
    for x in b:
        d[x] -= 1
    return not any(d.values())

if __name__ == "__main__":
    primes = [ p for p in primes_sieve(10000) if len(str(p)) == 4]

    memo = dict()
    for p in primes:
        for item, value in memo.items():
            if same_permutation(str(p), str(item)):
                memo[item] = memo[item] + [p]
        else:
            memo[p] = [p]

    primes = [sorted(vs, reverse=True) for vs in memo.values()]

    c = primes

    for p in primes:
      memo = defaultdict(int)
      for x in range(len(p)):
          for y in range(x):
              if memo[p[y] -p[x]]:
                  bar = memo[p[y] -p[x]]
                  bar.add(p[x])
                  bar.add(p[y])
                  memo[p[y] -p[x]] = bar
              else:
                  memo[p[y] -p[x]] = set([p[x],p[y]])

      for vs in memo.values():
          if len(vs) == 3:
              print("".join([str(_)for _ in vs]))


