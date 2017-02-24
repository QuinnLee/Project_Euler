'''
Find the maximum total from top to bottom of the triangle below:
'''
from functools import reduce

def rollup(bottom_row, top_row):
    new_row = []
    for index, value in enumerate(top_row):
        new_row.append(value+max(bottom_row[index:index+2]))

    return new_row

def max_path(triangle):
    dup_triangle = list(triangle)
    dup_triangle.reverse()
    return reduce(rollup, dup_triangle)[0]

if __name__ == "__main__":
    with open('files/p067_triangle.txt') as f:
        lines = f.read().splitlines()
    triangle = [[ int(x) for x in line.split(' ') ]  for line in lines]


    print(triangle)
    print(max_path(triangle))

