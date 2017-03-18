'''
It is possible to show that the square root of two can be expressed as an infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

  1 + 1/2 = 3/2 = 1.5
  1 + 1/(2 + 1/2) = 7/5 = 1.4
  1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
  1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

  The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

  In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?
'''


if __name__ == "__main__":
    numerator = [1,1]
    denominator = [0,1]

    counter = 0
    for _ in range(1, 1000):
        n_1 = numerator[0]
        n_2 = numerator[1]

        d_1 = denominator[0]
        d_2 = denominator[1]

        n = 2 * n_2 + n_1

        numerator = [n_2, n]

        d = 2 * d_2 + d_1

        denominator = [d_2, d]

        if(len(str(n)) > len(str(d))):
            counter = counter + 1
        print(n/d)


    print(counter)
