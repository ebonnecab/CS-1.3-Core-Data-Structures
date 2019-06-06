#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests

    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    
    if array[0] == item:
        return 0
    
    elif array[1] == item:
        return 1

    elif array[index] == item:
        return index

    return linear_search_recursive(array, item, index+1)
            
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    #implement binary search iteratively here
    first = 0
    last = len(array) -1
    position = None
    found = False

    while not found and first <= last:
        midpoint = (first + last) //2
        if array[midpoint] == item:
            found = True
            position = midpoint
    
        #if item is smaller than midpoint ignore the right
        elif item < array[midpoint]:
            last = midpoint -1
        #if item is greater than midpoint ignore the left
        elif item > array[midpoint]:
            first = midpoint+1
    return position


    
def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    position = None
    left = 0
    right = len(array)-1
    
    if right >= left:
        midpoint = (left + right) // 2

        if array[midpoint] == item:
            position = midpoint
        elif array[midpoint] > item:
            return binary_search_recursive(array, item, left=0, right=midpoint-1)
        elif array[midpoint] < item:
            return binary_search_recursive(array, item, left=midpoint+1, right=right)

    return position

    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
