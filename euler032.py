'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''

from collections import Counter

def pandigital(low, high):
  DIGITS = Counter([ str(num) for num in range(low, high+1)])
  products = set()
  ms = set()

  for multiplicand in range(low, 10**4):
      multiplicand_counter = Counter(str(multiplicand))
      if len(set(multiplicand_counter.values())) != 1 or multiplicand in ms:
          continue

      for multiplier in range(low, 10**4):
          multiplier_counter = Counter(str(multiplier))
          if len(set((multiplier_counter + multiplicand_counter).values())) != 1 or multiplier in ms:
              continue

          product = multiplier * multiplicand
          string = str(product) + str(multiplicand) + str(multiplier)

          if len(string) > 9:
              break

          if DIGITS == Counter(string):
              products.add(product)
              ms.add(multiplier)
              ms.add(multiplicand)

  return products


if __name__ == "__main__":
      answer = pandigital(1,9)

      print(7254 in answer)
      print(answer)
      print(sum(answer))

