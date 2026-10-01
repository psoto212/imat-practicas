
# this can be sped up using numpy, i guess

def countSort(vec, TRACE=False):
    # assumes all values are positive integers 
    
    # get max
    # we can improve in space by looking into the minimal k, as well
    # in general this can be applied to a set of finite categories, that can be sorted...like characters
    k = max(vec)
    if TRACE: print (f"Max Key is {k}")
    
    # define the count vector with range 0 to k
    countVec = [0]*(k+1)        
    
    # accumulate the counts
    for item in vec:
        countVec[item] = countVec[item] + 1
    if TRACE: print (f"{countVec=}")    
       
    # accumulate
    for i_k in range(1,k+1):
        countVec[i_k] = countVec[i_k] + countVec[i_k-1]
    if TRACE: print (f"Accumulated {countVec=}")    
        
    # allocate sortedVec vector...
    sortedVec = [None] * len(vec)
    
    # position input vector as per the counts.... backwards
    for item  in reversed(vec):
        targetPos            = countVec[item]-1
        sortedVec[targetPos] = item
        countVec[item]      -= 1
    
    # Return the sorted vector
    return sortedVec

# driver code...
vec = [ 3,5,0,0,2,7,9,12,0,1]
print (countSort(vec,True))

import random
import time



vec = random.choices(list(range(10)),k=200)
vecSafe = vec.copy()
vecSafe.sort()
sortedVec = countSort(vec,True)
assert(vecSafe == sortedVec )

n = 100
ns = []
ops = []
nmax = 1E7
while n < nmax:
    ns.append(n)
    vec = random.choices(list(range(10)),k=n)
    vecSafe = vec.copy()
    vecSafe.sort()
    t0 = time.process_time()
    sortedVec = countSort(vec)
    assert(vecSafe == sortedVec )
    ell = time.process_time() - t0
    ops.append(ell)
    print (ns[-1],ops[-1])
    n = int(1.33 * n)

# lets drawit to check linearity of the sorting...
import matplotlib.pyplot as plt
fig, axes = plt.subplots(1,1,figsize=(8,8) )
axes.plot(ns, ops)
axes.grid()
plt.show()

