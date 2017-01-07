'''
A unit fraction contains 1 in the numerator.
The decimal representation of the unit fractions with denominators 2 to 10 are given:
  1/2  =   0.5
  1/3  =   0.(3)
  1/4  =   0.25
  1/5  =   0.2
  1/6  =   0.1(6)
  1/7  =   0.(142857)
  1/8  =   0.125
  1/9  =   0.(1)
  1/10  =   0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in
its decimal fraction part.
'''

'''
notes
https://en.wikipedia.org/wiki/Repeating_decimal#Decimal_expansion_and_recurrence_sequence
'''

def digit_cycle(denominator, numerator=1):
    remainders = set()
    cycle = ''

    while numerator not in remainders:
      remainders.add(numerator)
      cycle += str((numerator * 10) // denominator)
      numerator = (numerator * 10) % denominator

    return cycle, denominator

if __name__ == "__main__":
    one_div_seven  = digit_cycle(7)
    print(one_div_seven)

    one_div_three  = digit_cycle(3)
    print(one_div_three)

    one_div_twenty_nine = digit_cycle(29)
    print(one_div_twenty_nine)

    answer = max([digit_cycle(_) for _ in range(1, 1001)], key=lambda x: len(x[0]))

    print(answer)


