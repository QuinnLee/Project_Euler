
'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

from math import factorial

if __name__ == "__main__":

  answer = [ num for num in range(10, factorial(9))\
      if sum([factorial(int(char)) for char in str(num)]) == num]
  print(answer)
  print(sum(answer))
