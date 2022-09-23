'''
Expected Time Complexity: O(n.Logn)
Expected Auxiliary Space: O(n + m)
'''

class Solution():
    def heapify(self,a,n,i):
        largest=i
        l=2*i+1
        r=2*i+2
        
        if l<n and a[l]>a[largest]:
            largest=l
            
        if r<n and a[r]>a[largest]:
            largest=r
            
        if largest!=i:
            a[i],a[largest]=a[largest],a[i]
            self.heapify(a,n,largest)
        
    def mergeHeaps(self, a, b, n, m):
        #your code here
        for i in range(m):
            a.append(b[i])
            
        n=n+m # or n=len(a)
        
        for i in range(n//2,-1,-1):
            self.heapify(a,n,i)
            
        return a
        