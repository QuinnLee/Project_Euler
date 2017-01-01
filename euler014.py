'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

'''

def sequence(number):
    count = 0
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3*number + 1
        count +=1

    return count


def longest_sequence(limit):
    memo = (0,0)

    for number in range(1, limit):
        count = sequence(number)

        if count > memo[0]:
            memo = (count, number)

    return memo
if __name__ == "__main__":
    print(longest_sequence(10))
    print(longest_sequence(10**6))


