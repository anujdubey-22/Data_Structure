#     for better appraoch use Kernighan’s Algorithm : x and -x
#     Time Complexity : theta(logn)
class Solution:
	def setBits(self, N):
		# code here
		count=0
		while N:
		    if N==1:
		        count+=1
		    elif N%2==1:
		        count+=1
		        
	        N=N//2
	        
	        
	    return count


#      appraoch use Kernighan’s Algorithm : x and -x
#      Time Complexity : O(logn)
class Solution:
	def setBits(self, N):
		# code here
		count=0
		while N :
		    rsb=(N & -N)
		    N=N-rsb
		    count+=1
		    
	    return count