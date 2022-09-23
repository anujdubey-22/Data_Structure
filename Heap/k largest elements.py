'''
Expected Time Complexity: O(N + KlogK)
Expected Auxiliary Space: O(K+(N-K)*logK)
'''

class Solution:
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
            
        
	def kLargest(self,arr, n, k):
		# code here
		n=len(arr)
		ans=[]
		for i in range(n//2,-1,-1):
		    self.heapify(arr,n,i)
		    
	    count=1
	    for i in range(n-1,-1,-1):
	        if count==k:
	            ans.append(arr[0])
	            return ans 
	        else:
	            ans.append(arr[0])
	            arr[0],arr[i]=arr[i],arr[0]
	            self.heapify(arr,i,0)
	        count+=1
	    return ans