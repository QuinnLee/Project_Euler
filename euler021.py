'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
from math import ceil, sqrt

def proper_divsors_sum(number):
    divisors = set([1.0])
    half_way_point = int(ceil(sqrt(number)))

    for n in range(1, half_way_point):
        divisor = number / n
        if divisor.is_integer() and divisor != number:
            divisors.add(n)
            divisors.add(divisor)

    return sum(list(divisors))

def amicable_numbers(numbers):
    amicable_set = set()
    for number in numbers:
        n1 = proper_divsors_sum(number)
        if not n1.is_integer():
            continue
        if n1 == number:
            continue
        if n1 not in amicable_set and proper_divsors_sum(n1) == number:
            amicable_set.add(n1)
            amicable_set.add(number)

    return list(amicable_set)

if __name__ == "__main__":
      answer = amicable_numbers(range(1,10001))
      print(answer)
      print(sum(answer))

