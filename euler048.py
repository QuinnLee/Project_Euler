'''
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
'''

def sumseries(limit = 1000):
    return sum([ n **n for n in range(1, limit+1)])

if __name__ == "__main__":
    answer = str(sumseries())
    print(answer[-10:])
