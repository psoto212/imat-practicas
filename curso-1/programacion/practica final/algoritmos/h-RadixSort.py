# Python program for implementation of Radix Sort
# A function to do counting sort of arr[] according to
# the digit represented by exp.


def countingSort(arr, exp1):
	n = len(arr)
	output = [None] * (n)                                               # The output array elements that will have sorted arr
	count = [0] * (10)                                                  	# initialize count array as 0
	for ele in arr:                                                      	# Store count of occurrences in count[]
		index = ele // exp1
		count[index % 10] += 1             
	for i in range(1, 10):                                                  # Change count[i] so that count[i] now contains actual
		count[i] += count[i - 1]                                            # position of this digit in output array
	i = n - 1                                                             # Build the output array
	while i >= 0:
		index = arr[i] // exp1
		output[count[index % 10] - 1] = arr[i]
		count[index % 10] -= 1
		i -= 1
	i = 0                                                             # Copying the output array to arr[],
	for i in range(0, len(arr)): 											# so that arr now contains sorted numbers
		arr[i] = output[i]
def radixSort(arr):													# Method to do Radix Sort
	max1 = max(arr)													# Find the maximum number to know number of digits
	exp = 1													# Do counting sort for every digit. Note that instead	
	while max1 / exp >= 1:										# of passing digit number, exp is passed. exp is 10^i
		countingSort(arr, exp)									# where i is current digit number
		exp *= 10
# Driver code
arr = [170, 45, 75, 90, 802, 24, 2, 66]
# Function Call
radixSort(arr)
for i in range(len(arr)):
	print(arr[i], end=" ")

