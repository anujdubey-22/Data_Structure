'''  
Given an array A containing 2*N+2 positive numbers, 
out of which 2*N numbers exist in pairs whereas the other two number occur exactly once and are distinct. 
Find the other two numbers.
'''

# Expected Time Complexity: O(N)
# Expected Space Complexity: O(1)

class Solution:
	def singleNumber(self, nums):
		# Code here
		xor=nums[0]
		for i in range(1,len(nums)):
		    xor =xor ^ nums[i]
		    
		rsb= xor & -xor
		x=0
		y=0
		for i in range(len(nums)):
		    if (nums[i] & rsb)==0:
		        x = x ^ nums[i]
		        
		    else:
		        y= y ^ nums[i]
		arr=[]       
	    if x<y:
	        arr.append(x)
	        arr.append(y)
	    else:
	        arr.append(y)
	        arr.append(x)
	        
	    return arr
