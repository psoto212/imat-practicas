import random
def bubbleSort(vec,TRACE=False):
    n = len(vec) 
    count =0
    print (f"pass: {count}: {vec}")
    while True:
        swaps = False
        count += 1
        for i in range(1, n):
            if vec[i-1] > vec[i]:
                vec[i-1],vec[i] = vec[i],vec[i-1]
                swaps = True
        print (f"pass: {count}: {vec} {swaps=}")
        if not swaps: 
            if TRACE: print (f"Bubble2 iterated {count} times on vector length {n}")
            break
    return    


def bubbleSortV2(vec):
    """_Improved bubble sort_

    Args:
        vector of comparable elements
        vector is sorted in place
        No return
    """
    n = len(vec)
    for i in range(1, n-1):
        for j in range(n-1, i-1, -1):
            if vec[j-1] > vec[j]:
                vec[j-1],vec[j] = vec[j],vec[j-1]
    return
# testTimes = 10
# for _ in range(testTimes):
#     vecbase = [ random.random() for _ in range (1000)]
#     vec = [ ele for ele in vecbase]
#     vecbase.sort()
#     bubbleSort(vec)
#     try:
#         assert(vecbase == vec)
#         print ("Bubble sort test ok")
#     except:
#         print ("test Failed")


vec2 = [4,2,6,7,0,3,5]
bubbleSort(vec2)


    
    