import random
def minmax(vec):

    # define a short utility function
    def _minmax2(a, b):
        if a < b:
            return a, b
        else:
            return b, a

    if len(vec) == 0:
        raise Exception("MinMax: empty Sequence")

    if len(vec) < 2:
        return vec[0], vec[0]

    # set the start first
    if vec[1] > vec[0]:
        maxVal = vec[1]
        minVal = vec[0]
    else:
        maxVal = vec[0]
        minVal = vec[1]

    # handle off-lenghts
    if (len(vec) % 2 == 1):
        top = len(vec) - 3
    else:
        top = len(vec) - 2

    for i in range(2, top):
        lmin, lmax = _minmax2(vec[i], vec[i+1])
        minVal = _minmax2(minVal, lmin)[0]
        maxVal = _minmax2(maxVal, lmax)[1]

        if lmin < minVal:
            minVal = lmin
        if lmax > maxVal:
            maxVal = lmax

    # handle the odd element
    if (len(vec) % 2 == 1):
        minVal = _minmax2(minVal, vec[-1])[0]
        maxVal = _minmax2(maxVal, vec[-1])[1]

    return minVal, maxVal


def findMedian1(vec,iz,de,k):
    if (iz == de):
        return vec[iz]

    vec,d = qs_divide(vec,iz,de)
    tm_iz  = d - iz +1;
    
    if (k  <= tm_iz ):
        val = findMedian1(vec, iz, d, k);
    else:
        val = findMedian1(vec, d+1, de, k-tm_iz);
        
    return val 

def findMedian(vec, DEBUG=False):
    """
    Median calcuation
    this algorithm destroys the order of the vector....

    Args:
        vec (_type_): _description_
        DEBUG (bool, optional): _description_. Defaults to False.

    Returns:
        _type_: _description_
    """

    def _findOrderedVal(vec, offset, targetPos, DEBUG=DEBUG):

        if DEBUG: print(f"{vec=} {offset=} {targetPos=}")

        # terminal Case, jsut return the value...
        if len(vec) == 1:
            if DEBUG: print(f"Terminal Case reached,return")
            return vec[0]

        else:
            # Particiona vec con pivot aleatorio...
            d = qs_divide(vec)            
            
            if (offset + d > targetPos):
                val = _findOrderedVal(vec[:d], offset, targetPos, DEBUG=DEBUG)
            else:
                val = _findOrderedVal(vec[d:], offset+d, targetPos, DEBUG=DEBUG)

        return val

    # save the original order...
    # if vec is a vector of objects, only pointers are duplicated...
    savedOrder = [tupla for tupla in enumerate(vec)]

    # for odd length vectors just call the internal function
    if len(vec) % 2 == 1:
        val = _findOrderedVal(vec, 0, len(vec) // 2, DEBUG=DEBUG)
    
    # for even  lenght compute medians with -/+ splits and average
    else:
        val1 = _findOrderedVal(vec, 0, (len(vec)-1)//2,     DEBUG=DEBUG)
        val2 = _findOrderedVal(vec, 0, (len(vec)+1)//2, DEBUG=DEBUG)
        val = 0.5*(val1 + val2)

    # this restitutes the order of the vec argument....
    for tupla in savedOrder:
        vec[tupla[0]] = tupla[1]

    return val

def swap(vec, i, j):
    vec[i], vec[j] = vec[j], vec[i]

def qs_divide(vec, DEBUG=False):
    """ Divide un vector con un umbral RANDOM  en dos partes donde la 
        los elementos de la izq son MENOR o IGUAL que los de la derecha.
        return the index staring the second part of the divide
    """
    # lets deal with no range case where min and max of the range are equal
    theMin, theMax = minmax(vec)
    if theMin == theMax:
        return len(vec) // 2

    # select a random pivot and place it as first...
    umbral_index = random.randint(0, len(vec)-1)
    umbral = vec[umbral_index]
    swap(vec, 0, umbral_index)

    l_i = 1
    r_i = len(vec)-1
    while l_i < r_i:
        
        # these are the conditions for jumping...
        l_bigger  = vec[l_i] > umbral           
        r_smaller = vec[r_i] <= umbral
        if DEBUG: print(l_i, r_i, l_bigger, r_smaller, vec)

        # both conditions ok, swap and advance
        if l_bigger and r_smaller:            
            if DEBUG: print(f"swapping {vec[l_i]} at  {l_i} and {vec[r_i]} at {r_i}")
            swap(vec, l_i, r_i)
            l_i += 1; r_i -= 1
            
        # No match  because of left, advance left, keep right   
        elif not l_bigger and     r_smaller:       
            l_i += 1
            
        # no match because of right, decrement right, keep left
        elif     l_bigger and not r_smaller:       
            r_i -= 1
            
        # both miss , no swap, but advance...
        else:                             
            l_i += 1; r_i -= 1

    # decide where exactly is the partition index, so that from there on all elements
    # are bigger that unmbral
    if vec[l_i] > umbral:
        return l_i
    else:
        return l_i + 1
 
def quick_sort(vec, DEBUG=None):

    if DEBUG: print (vec)

    match len(vec):
        case 0:
            pass

        case 1:
            pass

        case 2:
            if vec[0] > vec[1]:
                swap(vec, 0, 1)

        case other:
            d = qs_divide(vec, DEBUG=False)
            if DEBUG: print(f"qs_divide at positions {d} into  {vec[:d]} and {vec[d:]}")
            vec[:d] = quick_sort(vec[:d],  DEBUG=DEBUG)         # do left  side
            vec[d:] = quick_sort(vec[d:],  DEBUG=DEBUG)         # do right side

    if DEBUG:
        print(f"returning {vec}")
    return vec

 
   
######################################################
# test
# n = 20
# vec = [ random.randint(-100,100) for _ in range(n)]
# quick_sort(vec)
# print (vec)
##################################

# import random
# import time
# import math
# import numpy as np
# n = 100
# ns = []
# ops = []
# nmax = 1E6
# while n < nmax:
#     ns.append(n)
#     vec = [ random.random() for _ in range(n)]
#     vec_safe = vec.copy()
#     t0 = time.process_time()
#     vec_safe.sort()
#     pySort = time.process_time() - t0
#     t0 = time.process_time()
#     quick_sort(vec, False)
#     assert(vec == vec_safe)   # test we are doing it right....
#     ell = time.process_time() - t0
#     ops.append(ell)
#     print (ns[-1],ops[-1],pySort)
#     n = int(1.33 * n)
    
# import matplotlib.pyplot as plt
# fig, axes = plt.subplots(1,2,figsize=(16,8) )
# axes[0].plot(ns, ops)
# axes[0].grid()
# axes[0].set_yscale('log')
# axes[0].set_xscale('log')

# nlogn = [ n*math.log(n) for n  in ns]
# redT = [ t/nlogn_val for t, nlogn_val in  zip(ops, nlogn)]
# axes[1].plot(ns,redT)
# axes[1].grid()
# plt.show()

# logn = [ math.log(n) for n  in ns]
# logt = [ math.log(t) for t in ops]
# fit = np.polyfit(logn,logt,1)
# print (fit)


# test median
# n = 2100
# vec = [ random.randint(-100,100) for _ in range(n)]
# med = findMedian(vec)
# up = sum( ele > med for ele in vec)
# down = sum( ele < med for ele in vec)

# print (med,up,down)
vec = [4,	3,	1,	9,	8,	5,	1,	2]

quick_sort(vec,True)

