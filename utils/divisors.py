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
