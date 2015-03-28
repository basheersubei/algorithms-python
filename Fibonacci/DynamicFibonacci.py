# this function performs Fibonacci using dynamic programming
import numpy as np


def dynamic_fib(x):
    # iteratively build up to the answer
    for i in range(2, x + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[x]


# initialize empty array
f = np.zeros((100))
# define base cases manually
f[0] = 0
f[1] = 1
# run it from 0 to 99
for i in range(100):
    print "fib(" + str(i) + ") is: " + str(dynamic_fib(i))
