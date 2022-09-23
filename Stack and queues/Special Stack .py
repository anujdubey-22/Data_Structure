'''
Expected Time Complexity: O(N) for getMin, O(1) for remaining all 4 functions.
Expected Auxiliary Space: O(1) for all the 5 functions
'''

import sys
def push(arr, ele):
    # Code here
    arr.append(ele)
    return 

# Function should pop an element from stack
def pop(arr):
    # Code here
    if len(stack)!=0:
        arr.pop()
    return 

# function should return 1/0 or True/False
def isFull(n, arr):
    # Code here
    if len(arr)>=n:
        return True
    else:
        return False

# function should return 1/0 or True/False
def isEmpty(arr):
    #Code here
    if len(arr)==0:
        return True
    else:
        return False

# function should return minimum element from the stack
def getMin(n, arr):
    # Code here
    get_min=sys.maxsize
    for i in range(len(arr)):
        if get_min>arr[i]:
            get_min=arr[i]
    return get_min
