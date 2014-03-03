memo = {0:0, 1:1}

def fib(n):
    if not n in memo:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

def even(n): return n % 2 == 0

def fib_array(max_number):
    array = []
    n = 1

    while max_number > fib(n):
        array.append(fib(n))
        n += 1

    return array

print sum(filter(even,fib_array(4000000)))
