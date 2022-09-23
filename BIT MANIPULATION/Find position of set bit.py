'''
Expected Time Complexity: O(log(N))
Expected Auxiliary Space: O(1)
'''
class Solution:
    def findPosition(self, N):
        # code here 
        if N==0:
            return -1
            
        count=0    
        if N &(N-1)==0:
            while N:
                count+=1
                N=N>>1
            return count
            
        return -1
            
  ###########################################################

import math
class Solution:
    def findPosition(self, N):
        # code here 
        if N==0:
            return -1
            
        count=0    
        if N &(N-1)==0:
            ans=math.log2(N)+1
            return int(ans)
            
        return -1
            