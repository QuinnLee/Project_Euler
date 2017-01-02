'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

NUMBER_DICT = {
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen',
    20:'twenty',
    30:'thirty',
    40:'forty',
    50:'fifty',
    60:'sixty',
    70:'seventy',
    80:'eighty',
    90:'ninety',
    100:'hundred',
    1000:'thousand'
}

def character_count(number):
    count = 0

    while number:
        if number // 1000:
            count += len(NUMBER_DICT[1000])
            count += len(NUMBER_DICT[number// 1000])
            number = number - (number// 1000) * 1000
        elif number // 100:
            count += len(NUMBER_DICT[100])
            count += len(NUMBER_DICT[number// 100])
            number = number - (number// 100) * 100
            if number:
              count += 3
        elif number < 100 and number >= 20:
            count += len(NUMBER_DICT[(number // 10)*10])
            number = number - (number// 10) * 10
        elif number < 20:
            count += len(NUMBER_DICT[number])
            number = 0
    return count

if __name__ == "__main__":
    print(character_count(342))
    print(character_count(115))
    print(character_count(1000))
    print(sum([character_count(_) for _ in range(1,6)]))
    print(sum([character_count(_) for _ in range(1,1001)]))
