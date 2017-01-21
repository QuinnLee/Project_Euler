'''
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''

from collections import Counter

if __name__ == "__main__":

    for i in range(1, 10**9):
        counter = Counter(str(i))

        if counter != Counter(str(i*2)):
           continue
        if counter != Counter(str(i*3)):
           continue
        if counter != Counter(str(i*4)):
           continue
        if counter != Counter(str(i*5)):
           continue
        if counter != Counter(str(i*6)):
           continue
        print(i)
        break
