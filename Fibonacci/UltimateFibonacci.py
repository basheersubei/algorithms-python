# this function performs Fibonacci using constant storage


def ultimate_fib(x):
    prev2 = 0  # holds value from fib i-2
    prev1 = 1  # holds value from fib i-1
    n = 0      # holds value for next fib
    if (x == 0):
        return 0

    for i in range(2, x):
        n = prev2 + prev1
        prev2 = prev1
        prev1 = n
    return prev1 + prev2

# run it from 0 to 99
for i in range(100):
    print "fib(" + str(i) + ") is: " + str(ultimate_fib(i))
