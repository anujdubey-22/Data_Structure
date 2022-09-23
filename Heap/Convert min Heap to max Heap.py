'''
Given array representation of min Heap, convert it to max Heap in O(n) time.

Expected Time Complexity : O(n)
'''

def heapify(a,i,n):
    largest=i
    left=2*i+1
    right=2*i+2
    
    if left<n and a[largest]<a[left]:
        largest=left
        
    if right<n and a[largest]<a[right]:
        largest=right
        
    if i!=largest:
        a[i],a[largest]=a[largest],a[i]
        heapify(arr,largest,n)

def solve(arr):
    n=len(arr)
    
    for i in range((n//2)-1,-1,-1):
        heapify(arr,i,n)
    return arr
    
    
arr = [3, 5 ,9, 6, 8, 20 ,10 ,12 ,18, 9]
print(solve(arr))