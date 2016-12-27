'''
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''


def largest_palindrome():
  number = 999 ** 2

  while number:
    to_string = str(number)

    mid = len(to_string)//2

    if to_string[:mid] == to_string[-1*mid:][::-1]:
        for _  in range(100, 999):
            if number % _ == 0 and (number//_) < 999:
                return number
    number -= 1

if __name__ == "__main__":
    print(largest_palindrome())
