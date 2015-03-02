# this function performs Insertion Sort
import math
import random
import sys
def InsertionSort(A):
	A[0] = -sys.maxint - 1
	for i in range(len(A))[1:]:
		j = i
		while (A[j] < A[j - 1]):
			A[j], A[j-1] = A[j-1], A[j] # swap A[j] and A[j-1]
			j = j - 1
	return A

arr = range(100)
random.shuffle(arr)

print "Array is: "
for a in arr:
	print a
print "Sorted array is: "
for s in InsertionSort(arr):
	print s
