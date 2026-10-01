# Python3 program to sort an array
# using bucket sort


def insertionSort(b):
	for i in range(1, len(b)):
		up = b[i]
		j = i - 1
		while j >= 0 and b[j] > up:
			b[j + 1] = b[j]
			j -= 1
		b[j + 1] = up
	return b


def bucketSort(x):
	arr = []
	slot_num = 10 # 10 means 10 slots, each
	# slot's size is 0.1
	for i in range(slot_num):
		arr.append([])

	# Put array elements in different buckets
	for j in x:
		index_b = int(slot_num * j)
		arr[index_b].append(j)

	# Sort individual buckets
	for i in range(slot_num):
		arr[i] = insertionSort(arr[i])

	# concatenate the result
	k = 0
	for i in range(slot_num):
		for j in range(len(arr[i])):
			x[k] = arr[i][j]
			k += 1
	return x


import random
import time 
n = 100
vec = [ random.random() for _ in range(n) ]
vecSafe = vec.copy()
vecSafe.sort()
sortedVec = bucketSort(vec)
assert(vecSafe == sortedVec )

n = 100
ns = []
ops = []
nmax = 1E5
while n < nmax:
    ns.append(n)
    vec = [ random.random() for _ in range(n) ]
    vecSafe = vec.copy()
    vecSafe.sort()
    t0 = time.process_time()
    sortedVec = bucketSort(vec)
    assert(vecSafe == sortedVec )
    ell = time.process_time() - t0
    ops.append(ell)
    print (ns[-1],ops[-1])
    n = int(1.33 * n)

# lets drawit to check linearity of the sorting...
import matplotlib.pyplot as plt
fig, axes = plt.subplots(1,1,figsize=(8,8) )
axes.plot(ns, ops)
axes.set_title("Bin_Sort performance")
axes.grid()
plt.show()