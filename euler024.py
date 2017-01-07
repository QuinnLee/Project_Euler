'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

from itertools import permutations
def generate_permutations(collection, limit):
    if not collection:
          return []

    if len(collection) == 1:
        return [collection]

    permuations_list  = list()
    for i, value in enumerate(collection):
        other_values = collection[:i] + collection[i+1:]
        for p in generate_permutations(other_values, limit):
            permuations_list.append([value] + p)
            if len(permuations_list) == limit:
                return permuations_list

    return permuations_list

if __name__ == "__main__":
    p1 = generate_permutations(list(range(0,10)), 10**6)
    print(p1[-1])

    p2 = list(permutations(range(0,10)))[10**6 - 1]
    print(p2)
