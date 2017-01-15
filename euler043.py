'''
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

  d2d3d4=406 is divisible by 2
  d3d4d5=063 is divisible by 3
  d4d5d6=635 is divisible by 5
  d5d6d7=357 is divisible by 7
  d6d7d8=572 is divisible by 11
  d7d8d9=728 is divisible by 13
  d8d9d10=289 is divisible by 17
  Find the sum of all 0 to 9 pandigital numbers with this property.
'''

from itertools import permutations

def pandigital(p_list):
  memo = list()

  for p in p_list:
      if not (int(p[1:4]) / 2).is_integer():
          continue
      if not (int(p[2:5]) / 3).is_integer():
          continue
      if not (int(p[3:6]) / 5).is_integer():
          continue
      if not (int(p[4:7]) / 7).is_integer():
          continue
      if not (int(p[5:8]) / 11).is_integer():
          continue
      if not (int(p[6:9]) / 13).is_integer():
          continue
      if not (int(p[7:10]) / 17).is_integer():
          continue

      memo.append(int(p))

  return memo

if __name__ == "__main__":
    p_list = list(map("".join, permutations('0123456789')))

    answer = pandigital(p_list)

    print(sum(answer))
