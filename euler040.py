'''

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

'''

from math import sqrt
from collections import Counter


if __name__ == "__main__":

    string = '0'
    count = 1

    while len(string) < 1000001:
      string += str(count)
      count += 1

    d1 = int(string[1])
    d10 = int(string[10])
    d100 = int(string[100])
    d1000 = int(string[1000])
    d10000 = int(string[10000])
    d100000 = int(string[100000])
    d1000000 = int(string[1000000])
    answer = d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000
    print(answer)
