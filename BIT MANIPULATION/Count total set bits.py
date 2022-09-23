'''
You are given a number N. Find the total count of set bits for all numbers from 1 to N(both inclusive).
'''
'''
     Expected Time Complexity: O(log N).
     Expected Auxiliary Space: O(1).
'''
class Solution:
    def findPowerOfTwo(self,n):
        x=0
        while  (1<<x)<=n:
            x+=1
            
        return x-1
    #Function to return sum of count of set bits in the integers from 1 to n.
    def countSetBits(self,n):
        # code here
        # return the count
        if n <=1:
            return n
            
        x=self.findPowerOfTwo(n)
        
        return ((x*(1<<(x-1))) + n-(1<<x)+1 + self.countSetBits(n-(1<<x)))
 