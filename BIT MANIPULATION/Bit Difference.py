'''
You are given two numbers A and B. The task is to count the number of bits needed to be flipped to convert A to B.
'''

''' 
Expected Time Complexity: O(log N).
Expected Auxiliary Space: O(1). 
'''


class Solution:
    ##Complete this function
    # Function to find number of bits needed to be flipped to convert A to B
    def countBitsFlip(self,a,b):
        ##Your code here
        count=0
        ans= a ^ b
        
        while ans:
            rsb= ans & -ans
            
            ans-=rsb
            count+=1
            
        return count
