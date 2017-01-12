'''

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

'''

''' notes

a + b + c = p

sqrt(a^2 + b ^2) = c

a + b + sqrt(a^2 + b ^2)  = p

'''

from math import sqrt
from collections import Counter


def intergal_sides(p=1000):
    counter = Counter()

    memo = set()
    for a in range(1, p+1):
        for b in range(1, p+1):
            c = sqrt(a**2 + b**2)
            f_set = frozenset([a,b,c])
            if c.is_integer() and f_set not in memo and a+b+c <= p:
                memo.add(f_set)
                counter[c+b+a] +=1

    return counter

if __name__ == "__main__":
    answer = intergal_sides()
    print(answer.most_common(1))
