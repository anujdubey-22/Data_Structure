'''
Expected Time Complexity: O(log N).
Expected Auxiliary Space: O(1).
'''
class Solution:
    ##Complete this function
    # Function to check if given number n is a power of two.
    def isPowerofTwo(self,n):
        ##Your code here
        
        if n<1:
            return False
        if n==1:
            return True
            
        x=0
        while (1<<x)<n:
            x+=1
            
        if (1<<x)==n:
            return True    
        return False


################################################################

class Solution:
    ##Complete this function
    # Function to check if given number n is a power of two.
    def isPowerofTwo(self,n):
        ##Your code here
        if n<1:
            return False
        val= n & (n-1)
        if val==0:
            return True
        else:
            return False