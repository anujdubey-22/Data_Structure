'''
Expected Time Complexity : O(nlogn)
Expected Auxilliary Space : O(n) 
'''

import heapq
class Solution:
    #Function to return the minimum cost of connecting the ropes.
    def minCost(self,arr,n) :
    
        # code here
        sum=0
        cost=0
        heapq.heapify(arr)
        while len(arr)>1:
            x=heapq.heappop(arr)
            y=heapq.heappop(arr)
            sum=x+y
            cost+=sum
            heapq.heappush(arr,sum)
            
        return cost