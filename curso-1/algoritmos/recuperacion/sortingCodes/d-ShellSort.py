
import math
import time
import  numpy as np
def shell_sort(vec,steps, TRACE=False):
    
    ops = 0 
    
    if steps is None:
        steps = []
        i = int(len(vec) / math.log2(len(vec)))
        while i > 0:
            steps.append(i)
            i = i // 2
    
    print (f"Shell sort length={len(vec)}, {steps=}")

    # iterate on the steps
    for step in steps:
        if TRACE: print (f"Using Step {step}")
        # it replicates the insertion sort with a step...
        
        for i in range(step, len(vec)):              # empieza en el segundo elementos
            aux = vec[i]; ops += 1
            if TRACE: print (f"Searching  position for index {i}")
            j = i-step
            while (j >= 0) and ( aux< vec[j]) :
                vec[j+step] = vec[j] ;  ops += 1
                j -= step
                
                
            if i != (j+step):
                if TRACE: print (f"Moving pos {i} into pos {j+step}")
                vec[j+step] = aux ; ops += 1    

    return vec, ops

import random
n = 100
ns = []
ops = []
nmax = 1E7
while n < nmax:
    ns.append(n)
    vec = [ random.random() for _ in range(n)]
    vec_safe = vec.copy()
    t0 = time.process_time()
    vec_safe.sort()
    pySort = time.process_time() - t0
    t0 = time.process_time()
    shell_sort(vec,None, False)
    assert(vec == vec_safe)   # test we are doing it right....
    ell = time.process_time() - t0
    ops.append(ell)
    print (ns[-1],ops[-1],pySort)
    n = 2 * n
    
import matplotlib.pyplot as plt
fig, axes = plt.subplots(1,2,figsize=(16,8) )
axes[0].plot(ns, ops)
axes[0].grid()
axes[0].set_yscale('log')
axes[0].set_xscale('log')

nlogn = [ n*math.log(n) for n  in ns]
redT = [ t/nlogn_val for t, nlogn_val in  zip(ops, nlogn)]
axes[1].plot(ns,redT)
axes[1].grid()
plt.show()

logn = [ math.log(n) for n  in ns]
logt = [ math.log(t) for t in ops]
fit = np.polyfit(logn,logt,1)
print (fit)
