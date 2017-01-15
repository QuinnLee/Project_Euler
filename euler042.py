'''
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

  1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

  By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

  Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

'''
from utils.letters import LETTER_MAPPING

def triangle_numbers(limit=10**5):
    memo = []

    for _ in range(1, limit):
        n = int(((_)) * (_ + 1)/2)
        memo.append(n)

    return set(memo)

def letter_value(name):
    return sum([LETTER_MAPPING[char] for char in name])

def triangle_names(names):
    triangle_n = triangle_numbers()
    return [name for name in names if int(letter_value(name)) in triangle_n]



if __name__ == "__main__":
    with open('files/p42_words.txt', 'r') as f:
        lines = f.readlines()[0]
        lines = lines.replace('"', '').strip().split(',')
        lines = sorted(lines)
        answer = triangle_names(lines)
        print(answer)
        print(len(answer))
