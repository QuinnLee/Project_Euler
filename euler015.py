'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''

'''
notes
Shortest-path Diagrams
central binomial coefficients
(2n)!/n!^2
'''
from math import factorial
if __name__ == "__main__":
      print(int(factorial(2*20)/(factorial(20)**2)))


