'''
The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053).
In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
'''

from collections import defaultdict


if __name__ == "__main__":
    done = False
    counter = 1
    memo = defaultdict(list)
    while not done:
        string = "".join(sorted(str(counter**3)))
        cubes = memo[string]
        cubes.append(counter)

        if(len(cubes) > 4):
            done = True

        counter += 1


    print(cubes[0] ** 3)


