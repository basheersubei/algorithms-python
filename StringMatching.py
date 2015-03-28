# this function performs string matching using Dynamic Programming
import sys


# given strings x and y, and 2d list alpha containing distances,
# and delta (cost for gap), return least cost for matching
def string_match(x, y, alpha, delta):

    # add an empty space at beginning just to fix table
    x = " " + x
    y = " " + y

    # get the string lengths and add 1
    m = len(x)
    n = len(y)

    # create an m x n list
    M = []
    for i in range(m):
        M.append([None] * n)

    # define base cases (first row and first column)
    for i in range(m):
        M[i][0] = delta * i
    for i in range(n):
        M[0][i] = delta * i

    for i in range(1, m):
        for j in range(1, n):
            if (i != 0 and j != 0):
                M[i][j] = min(
                    alpha[x[i]][y[j]] + M[i - 1][j - 1],
                    delta + M[i - 1][j],
                    delta + M[i][j - 1]
                )
    return M


def reconstruct_path(M, x, y, alpha, delta):
    # start at last element in M, and go backwards
    val = M[-1][-1]
    # get the string lengths
    m = len(x)
    n = len(y)
    row = m - 1  # current row
    col = n - 1  # current column

    # print first two numbers
    sys.stdout.write(str(M[row + 1][col + 1]))
    sys.stdout.write(str(M[row][col]))

    while(row > 0 and col > 0):
        diag = alpha[x[row]][y[col]] + M[row - 1][col - 1]
        left = delta + M[row][col - 1]
        up = delta + M[row - 1][col]
        # if diag is the min, go diagonally
        if (diag < min(left, up)):
            row -= 1
            col -= 1

        # if left is the min, go left
        elif (left < min(diag, up)):
            col -= 1
        # if up is the min, go up
        elif (up < min(diag, left)):
            row -= 1

        # just in case there's a draw, pick up first
        elif (up == left or up == diag):
            row -= 1
        elif (left == diag):
            col -= 1
        # sanity check
        else:
            print "Sanity lost!"

        sys.stdout.write(str(M[row][col]))
    # end while

    # last case
    if (row > 0):
        row -= 1
        sys.stdout.write(str(M[row][col]))
    elif (col > 0):
        col -= 1
        sys.stdout.write(str(M[row][col]))

    print ""

string1 = "Hello"
string2 = "Hallo"

# string1 = "CTACCG"
# string2 = "TACATG"

m = len(string1)
n = len(string2)

# all costs are 1 except for diagonal,
# this gives an mxn dictionary with all 1s except diagonal is zeros
alpha = {}
for i in range(ord('A'), ord('z')):
    alpha[chr(i)] = {}
    for j in range(ord('A'), ord('z')):
        if i == j:
            alpha[chr(i)][chr(j)] = 0
        else:
            alpha[chr(i)][chr(j)] = 1
# for example, the cost for substituting 'A' with 'B' is found in
# alpha['A']['B'] and equals 1

# delta is the cost of a single gap
delta = 1

# match the two strings, and return and print the 2d array with costs
M = string_match(string1, string2, alpha, delta)

# very ugly code just to print out the table with headers
sys.stdout.write("\t-\t")
for c in string1:
    sys.stdout.write(c + "\t")
print "\n"
for (first, row) in zip("-" + string2, M):
    sys.stdout.write(first + ":\t")
    for c in row:
        sys.stdout.write(str(c) + "\t")
    print ""

# much simpler code to print out table without top row label
# print('\n'.join('{}: {}'.format(*k) for k in zip(string2, M)))


# the optimal cost is the bottom-right (last) element in M
print "The optimal cost is: " + str(M[-1][-1])

reconstruct_path(M, string1, string2, alpha, delta)
