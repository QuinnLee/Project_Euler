'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''

from collections import Counter

def curious_fractions(digits=2):
    memo = []
    for denominator in range(1, 10**digits):
        for numerator in range(1, denominator):
            denominator_set = set(str(denominator))
            numerator_set = set(str(numerator))

            d1 = list(denominator_set - numerator_set)
            n1 = list(numerator_set - denominator_set)

            if '0' in numerator_set or '0' in denominator_set:
              continue

            if not d1 or not n1:
              continue

            if len(d1) == len(denominator_set) or len(n1) == len(numerator_set):
              continue

            if int(d1[0]) == 0 or int(n1[0]) == 0:
              continue

            if int(n1[0])/int(d1[0]) == numerator/denominator:
                print(numerator, denominator)
                memo.append((numerator/denominator, int(n1[0]), int(d1[0])))

    return memo

if __name__ == "__main__":
      answer = curious_fractions()

      print(answer)

