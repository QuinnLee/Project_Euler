'''
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)

'''

def palindromic_numbers(limit=10**6):
    numbers = list()
    for number in range(1, limit+1):
        string = "{0:b}".format(number)
        string_2 = "{0:d}".format(number)
        if string[0] == "0":
            continue

        if string[-1] == "0":
            continue

        if string[::-1] == string and string_2[::-1] == string_2:
            numbers.append(number)
            print(string_2)

    return numbers


if __name__ == "__main__":
    print(sum(palindromic_numbers()))
