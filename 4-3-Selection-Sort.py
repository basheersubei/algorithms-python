# this function performs Selection Sort, assuming min is a logn operation (just
# an example to explain basics of heapsort)
import math
import random
def SelectionSort(A):
	Sort = [0]*len(A)  # empty array of size A
	for i in range(len(A)):
		Sort[i] = min(A)
		A.remove(Sort[i])
	return(Sort)

arr = range(100)
random.shuffle(arr)

print "Array is: "
for a in arr:
	print a
print "Sorted array is: "
for s in SelectionSort(arr):
	print s
