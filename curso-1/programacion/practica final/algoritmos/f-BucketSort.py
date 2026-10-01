import math

def insertion_sort(vec, first, last):
    """insertion Sort
    vec must expose the sequence interface
    and vec elements must be comparables among themselves_summary_

    Args:
        vec (_type_): _description_
        sort_by (_type_, optional): _description_. Defaults to None.

    Returns:
        _type_: sorted
    """

    length = last - first + 1

    for i in range(first, last+1):       # start on the second element and on...
        vec_element = vec[i]           # lets take  the elemen ...

        # starting in the previous to the one taken, and backwards, compare
        j = i-1
        # compare the jth element against- element
        while (j >= first) and (vec_element < vec[j]):
            # push right the j element into J+1 position if vec(j) > element
            vec[j+1] = vec[j]
            j -= 1                 # go left for next

        # when reached the begining  ( j= -1) or when element is >+  vec(j)
        # place the element in the j+1 position
        vec[j+1] = vec_element

    return vec

def bin_sort(vec, nbins=None, DEBUG=None):

    def _bin(aVal, minVal, maxVal, nbins):
        if minVal >= maxVal:
            raise Exception(
                f"binning function: ranges wrong,{minVal=},{maxVal=} Uniform sequence ?")
        return math.floor(nbins*(aVal - minVal)/(maxVal*1.01-minVal))

    # determine the right num of bins
    if nbins is None:
        if len(vec) <= 10:
            nbins = 3
        else:
            nbins = int(math.log2(len(vec)))
            # nbins = len(vec) // 8  # lets make nbins O(N)
        print(f"bin_sort: no nbins specified, taken {nbins=} for {len(vec)=}")

    # allocate the bins
    bins = [[] for _ in range(nbins)]

    
    # podríamos utilizar la versión concurrent del cálculo de Min y Max
    minVal = min(vec) 
    maxVal = max(vec)
    if DEBUG: print(f"{minVal=}, {maxVal=}")

    # make outplaces[ibin] have the list of the elements on the ibin
    for element in vec:
        binNum = _bin(element, minVal, maxVal, nbins)
        bins[binNum].append(element)

    # reorganize the vec
    # place the elements back in vec, in bin order first
    index = 0
    for binList in bins:
        for element in binList:
            vec[index] = element
            index += 1

    #  now sort each subsection with
    i_start = 0
    for ibin in range(nbins):
        subLength = len(bins[ibin])
        if subLength > 1:
            if DEBUG: print(f"bin_Sort using insertion sort on vec[{i_start},{i_start+subLength}]")
            insertion_sort(vec,i_start,i_start+subLength-1)
        i_start += subLength

    return vec

############################################################333
# Testing the Code

import random
import time 
n = 100
vec = [ random.random() for _ in range(n) ]
vecSafe = vec.copy()
vecSafe.sort()
sortedVec = bin_sort(vec,True)
assert(vecSafe == sortedVec )

# # lets drawit to check linearity of the sorting...
import matplotlib.pyplot as plt
fig, axes = plt.subplots(2,1,figsize=(20,8) )

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
    sortedVec = bin_sort(vec)
    assert(vecSafe == sortedVec )
    ell = time.process_time() - t0
    ops.append(ell)
    print (ns[-1],ops[-1])
    n = int(1.33 * n)


axes[0].plot(ns, ops)
axes[0].set_title("Bin_Sort performance bins $\sim \log n $")
axes[0].grid()

n = 100
ns = []
ops = []
nmax = 1E6
while n < nmax:
    ns.append(n)
    vec = [ random.random() for _ in range(n) ]
    vecSafe = vec.copy()
    vecSafe.sort()
    t0 = time.process_time()
    nbins = int(n/8)
    sortedVec = bin_sort(vec,nbins)
    assert(vecSafe == sortedVec )
    ell = time.process_time() - t0
    ops.append(ell)
    print (ns[-1],ops[-1])
    n = int(1.33 * n)
    
axes[0].set_title("Bin_Sort performance bins $\sim n/8 $")
axes[1].plot(ns, ops,'r') 
axes[1].grid()

plt.show()

