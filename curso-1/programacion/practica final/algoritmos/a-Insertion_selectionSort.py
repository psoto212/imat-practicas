
# Insertion Sort, binary Insertion Sort, and selection Sort
import math
import random

def insertion_sort(vec):
    """insertion Sort
    vec must expose the sequence interface
    and vec elements must be comparables among themselves_summary_

    Args:
        vec (_type_): _description_

    Returns:
        _type_: sorted
    """

    # builds the sort_func for the given attribute, if provided
    
    for i in range(1, len(vec)):       # start on the second element and on...
        vec_element = vec[i]           # lets take  the elemen ...

        # starting in the previous to the one taken, and backwards, compare
        j = i-1
        # compare the jth element against- element
        while (j >= 0) and (vec_element < vec[j]):
            # push right the j element into J+1 position if vec(j) > element
            vec[j+1] = vec[j]
            j -= 1                 # go left for next

        # when reached the begining  ( j= -1) or when element is >+  vec(j)
        # place the element in the j+1 position
        vec[j+1] = vec_element

    return vec


def binSearch(vec, element):
    """ Returns the index so that  vec[:index] < element, and vec[index:] >= element  """
    # place l and r to ends of vector
    l, r = 0, (len(vec)-1)

    # mientras que no sean el mismo o se crucen...
    while (r-l) > 1:
        index = (r+l) // 2                            # find a middle place
        if element == vec[index]:
            return index    # hit it directly
        elif element > vec[index]:
            l = index       # it is on the right side. Set l
        else:
            r = index - 1    # it is on the left side,  Set r
            # go back in the while

    if element >= vec[r]:
        return r
    elif element > vec[l]:
        return l
    else:
        return -1


def binary_insertion_sort(vec):
    """ uses binary search..."""

    for i in range(1, len(vec)):
        # lets take the first element bey the sorted region
        vec_element = vec[i]

        # must move after pos, check for first
        # search in the vector  from 0 till i-1
        pos = binSearch(vec[:i], vec_element)

        # do the shift backwards till pos, no comparison required
        for j in range(i-1, pos, -1):
            vec[j+1] = vec[j]

        # place the element in the right place
        vec[pos+1] = vec_element

    return vec


def selection_sort(vec):
    """
        selects the minimum and places at the beginning of the
        unsorted region
    """
    
    for i in range(0, len(vec)-1):

        # find the index of the minimum element in vec[i+1:] (the unsorted region)
        min_key, min_pos = vec[i], i
        for j in range(i+1, len(vec)):
            if vec[j] < min_key:
                min_key, min_pos = vec[j], j

        # now place it in position i shifting data as needed
        min_element = vec[min_pos]
        for k in range(min_pos-1, i-1, -1):
            vec[k+1] = vec[k]
        vec[i] = min_element

    return vec


# test section
safe = [random.randint(-10000, 10000) for _ in range(10000)]
safe_sorted = sorted(safe)
for sortFunction in [insertion_sort, binary_insertion_sort, selection_sort]:
    try: 
        vec = safe.copy()
        # assert raises an exception if the statemen evaluates to False
        assert(sorted(safe) == sortFunction(vec))
        print(f"{sortFunction.__name__} tests OK")
    except:
        print(f"** {sortFunction.__name__} Failed OK, retrying")
        
