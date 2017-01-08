'''
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

  21 22 23 24 25
  20  7  8  9 10
  19  6  1  2 11
  18  5  4  3 12
  17 16 15 14 13

  It can be verified that the sum of the numbers on the diagonals is 101.

  What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''

'''
notes

1 + 3 + 5 + 7 + 9
'''

def side_dimension(d=1):
    if d % 2 == 0:
      return 0

    total = 1
    start = 1
    addition = 2
    current_d = 1
    while current_d != d:
        for _ in range(4):
            start += addition
            total += start

        addition += 2
        current_d += 2

    return total

if __name__ == "__main__":

    print(side_dimension(5))
    print(side_dimension(1001))

