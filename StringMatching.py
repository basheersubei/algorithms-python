# this function performs string matching using Dynamic Programming.
# it solves problem1 for HW4 in CS 401.
# this code is stored on GitHub at:
# https://github.com/basheersubei/algorithms-python/blob/master/StringMatching.py
import sys

# given strings x and y, and 2d list alpha containing distances,
# and delta (cost for gap), return least cost for matching
def string_match(x, y, alpha):

    # add an empty space at beginning just to fix table
    x = "-" + x
    y = "-" + y

    # get the string lengths and add 1
    m = len(x)
    n = len(y)

    # create an m x n list
    M = []
    for i in range(m):
        M.append([None] * n)

    # define base cases (first row and first column)
    M[0][0] = 0
    for i in range(1, m):
        M[i][0] = alpha[x[i]]['-'] + M[i - 1][0]
    for i in range(1, n):
        M[0][i] = alpha['-'][y[i]] + M[0][i - 1]

    # fill in rest of array
    for i in range(1, m):
        for j in range(1, n):
            if (i != 0 and j != 0):
                M[i][j] = min(
                    alpha[x[i]][y[j]] + M[i - 1][j - 1],
                    alpha[x[i]]['-'] + M[i - 1][j],
                    alpha['-'][y[j]] + M[i][j - 1]
                )
    return M


def reconstruct_path(M, x, y, alpha):
    # get the string lengths
    m = len(x)
    n = len(y)
    row = m - 1  # current row
    col = n - 1  # current column

    # these strings will hold the two matched strings
    seq1 = ""
    seq2 = ""

    while(row > 0 and col > 0):
        diag = alpha[x[row]][y[col]] + M[row - 1][col - 1]
        left = alpha['-'][y[col]] + M[row][col - 1]
        up = alpha[x[row]]['-'] + M[row - 1][col]

        # if diag is the min, go diagonally
        if (diag < min(left, up)):

            # # if there was a cost, then it was a mismatch
            # if (alpha[x[row]][y[col]] > 0):
            #     print "mismatch " + x[row] + " and " + y[col]
            # # else it was a match
            # else:
            #     print "match " + x[row]

            seq1 += x[row]
            seq2 += y[col]
            row -= 1
            col -= 1
        # if left is the min, go left
        elif (left < min(diag, up)):
            seq1 += "-"
            seq2 += y[col]
            col -= 1
        # if up is the min, go up
        elif (up < min(diag, left)):
            seq1 += x[row]
            seq2 += "-"
            row -= 1
        # just in case there's a draw, pick up first
        elif (up == left or up == diag):
            seq1 += x[row]
            seq2 += "-"
            row -= 1
        elif (left == diag):
            seq1 += "-"
            seq2 += y[col]
            col -= 1
        # sanity check
        else:
            print "Sanity lost!"
    # end while

    if (row > 0 and col > 0):
        seq1 += x[row]
        seq2 += y[col]
    # gap, go up
    elif (row > 0):
        seq1 += x[row]
        seq2 += "-"
        row -= 1
    # gap, go left
    elif (col > 0):
        seq1 += "-"
        seq2 += y[col]
        col -= 1

    # print the strings in reverse
    print seq1[::-1]
    print seq2[::-1]


# string1 = "GATGTAACA"
# string2 = "ATTACC"
string1 = "GAT?TAACA"
string2 = "ATTACC"

# string1 = "CTACCG"
# string2 = "TACATG"

# all costs are 1 except for diagonal,
# this gives an mxn dictionary with all 1s except diagonal is zeros
alpha = {}
# for i in range(ord('A'), ord('z')):
#     alpha[chr(i)] = {}
#     for j in range(ord('A'), ord('z')):
#         if i == j:
#             alpha[chr(i)][chr(j)] = 0
#         else:
#             alpha[chr(i)][chr(j)] = 1
# for example, the cost for substituting 'A' with 'B' is found in
# alpha['A']['B'] and equals 1

# custom non-default table of alpha, includes deltas
for i in ['A', 'C', 'T', 'G', '-', '?']:
    alpha[i] = {}
alpha['A']['A'] = 0
alpha['A']['C'] = 0.1
alpha['A']['T'] = 0.1
alpha['A']['G'] = 0.2
alpha['A']['-'] = 0.1
alpha['A']['?'] = 0

alpha['C']['A'] = 0.2
alpha['C']['C'] = 0
alpha['C']['T'] = 0.3
alpha['C']['G'] = 0.3
alpha['C']['-'] = 0.1
alpha['C']['?'] = 0

alpha['T']['A'] = 0.5
alpha['T']['C'] = 0.2
alpha['T']['T'] = 0
alpha['T']['G'] = 0.4
alpha['T']['-'] = 0.2
alpha['T']['?'] = 0

alpha['G']['A'] = 0.4
alpha['G']['C'] = 0.4
alpha['G']['T'] = 0.2
alpha['G']['G'] = 0
alpha['G']['-'] = 0.2
alpha['G']['?'] = 0

alpha['-']['A'] = 0.2
alpha['-']['C'] = 0.2
alpha['-']['T'] = 0.1
alpha['-']['G'] = 0.1
alpha['-']['-'] = None
alpha['-']['?'] = 1e309  # pretty much infinity

alpha['?']['A'] = 0
alpha['?']['C'] = 0
alpha['?']['T'] = 0
alpha['?']['G'] = 0
alpha['?']['-'] = 1e309  # pretty much infinity
alpha['?']['?'] = 0

# delta is the cost of a single gap
# delta = 1

# match the two strings, and return and print the 2d array with costs
M = string_match(string1, string2, alpha)

# very ugly code just to print out the table with headers
# this doesn't work if there are gaps in string2
# sys.stdout.write("\t-\t")
# for c in string1:
#     sys.stdout.write(c + "\t")
# print "\n"
# for (first, row) in zip("-" + string2, M):
#     sys.stdout.write(first + ":\t")
#     for c in row:
#         sys.stdout.write(str(c) + "\t")
#     print ""

# fix formatting of floats to two decimal points
for (i, r) in enumerate(M):
    for (j, c) in enumerate(r):
        M[i][j] = float(format(c, '.2f'))
# much simpler code to print out table without top row label
print('\n'.join('{}:\t {}'.format(*k) for k in enumerate(M)))


# the optimal cost is the bottom-right (last) element in M
print "The optimal cost is: " + str(M[-1][-1])

# go backwards from last element in M and reconstruct path to find
# two matched strings. The dash at the beginning is to correct the table.
reconstruct_path(M, "-" + string1, "-" + string2, alpha)
