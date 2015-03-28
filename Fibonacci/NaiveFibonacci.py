# this function performs Fibonacci using recursion


def fib(x):
    if (x == 0):
        return 0
    elif (x == 1):
        return 1
    else:
        return fib(x - 1) + fib(x - 2)

# run it from 0 to 99
for i in range(100):
    print "fib(" + str(i) + ") is: " + str(fib(i))
