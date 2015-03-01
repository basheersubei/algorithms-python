# this function performs "fast" exponentiation
import math
def power(a, n):
    if (n==0):
        return 1
    x = power(a, math.floor(n/2))
    if (n % 2 == 0):
        return x*x
    else:
        return a * x * x

bases       = range(10)
exponents   = range(5)
for base in bases:
    for exp in exponents:
        print "" + str(base) + " to the power of " + str(exp) + " is " + str(power(base, exp))


