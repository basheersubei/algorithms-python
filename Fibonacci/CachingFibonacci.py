# this function performs Fibonacci using caching
import numpy as np


def caching_fib(x):
    # if we haven't computed fib for that index, do it
    if (f[x] == 0 and x > 1):
        f[x] = caching_fib(x - 1) + caching_fib(x - 2)
    return f[x]


# initialize empty array
f = np.zeros((100))
# define base cases manually
f[0] = 0
f[1] = 1
# run it from 0 to 99
for i in range(100):
    print "fib(" + str(i) + ") is: " + str(caching_fib(i))
