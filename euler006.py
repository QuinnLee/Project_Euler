'''
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the
first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the
first one hundred natural numbers and the square of the sum.
'''

def difference_of_sum_squares(n):
  sum_of_square = 0
  square_of_sum = 0

  for number in range(1, n+1):
      sum_of_square += number ** 2
      square_of_sum += number

  return square_of_sum ** 2 - sum_of_square

if __name__ == "__main__":
    print(difference_of_sum_squares(10))
    print(difference_of_sum_squares(100))
