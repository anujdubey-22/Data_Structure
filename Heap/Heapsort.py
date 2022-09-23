'''
Time Complexity: Time complexity of heapify is O(Logn). Time complexity of createAndBuildHeap() is O(n) and the overall time complexity of Heap Sort is O(nLogn).
'''

def heapify(a,n,i):
    largest=i
    l=2*i+1
    r=2*i+2
    
    if l<n and a[l]>a[largest]:
        largest=l
        
    if r<n and a[r]>a[largest]:
        largest=r
        
    if largest!=i:
        a[i],a[largest]=a[largest],a[i]
        heapify(a,n,largest)
    
    
def solve(a,k):
    n=len(a)
    for i in range(n//2,-1,-1):
        heapify(a,n,i)
    
   
    for i in range(n-1,-1,-1):
        
        a[0],a[i]=a[i],a[0]
        heapify(a,i,0)
        
    return a


arr = [1, 23, 12, 9, 30, 2, 50]
k=3
print(solve(arr,k))
