'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
from collections import Counter
from functools import reduce

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def smallest_number_div(numbers):
  c = Counter()
  for n in numbers:
      c = Counter(prime_factors(n)) | c

  return reduce(lambda x, y: x*y, c.elements())


if __name__ == "__main__":
    print(smallest_number_div([1,2,3,4,5,6,7,8,9,10]))
    print(smallest_number_div(range(1,20)))

