'''
Expected Time Complxity : O(N)
Expected Auxilliary Space : O(N)
'''

import sys
class Solution:
    
    #Function to find largest rectangular area possible in a given histogram.
    def getMaxArea(self,arr):
        #code here
        stack=[]
        maxx=-sys.maxsize
        i=0
        while i<len(arr):
            if len(stack)==0 or arr[i]>=arr[stack[-1]]:
                stack.append(i)
                i+=1
                
            else:
                ind=stack.pop()
                if len(stack)==0:
                    area=arr[ind]*i
                else:
                    area=arr[ind]*(i-stack[-1]-1)
                maxx=max(maxx,area)
        while len(stack)>0:
            ind=stack.pop()
            if len(stack)==0:
                area=arr[ind]*i
            else:
                area=arr[ind]*(i-stack[-1]-1)
            maxx=max(maxx,area)
        return maxx
        
