'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''


'''
notes
a = sqrt(b^2+c^2)

'''

from math import sqrt

def pythagorean_triplet(total):
    for a in range(1,total):
      for b in range(a, total):
          c = sqrt(a**2 + b **2)
          if int(c) != c:
              continue
          if a + b + c == total:
              return int(a*b*c)

if __name__ == "__main__":
    print(pythagorean_triplet(1000))
