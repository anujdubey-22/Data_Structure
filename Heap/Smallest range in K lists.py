'''
Expected Time Complexity : O(n * k *log k)
Expected Auxilliary Space  : O(k)
'''

import heapq
class Solution:
   def smallestRange(self, numbers, n, k):
       minheap=[]
       maxx=-float('inf')
       for i in range(k):
           heapq.heappush(minheap,(numbers[i][0],i,0))
           maxx=max(numbers[i][0],maxx)
       heapq.heapify(minheap)
       diff=maxx-minheap[0][0]
       ans=[minheap[0][0],maxx]
       
       while True:
           mini,r,c=heapq.heappop(minheap)
           if diff>maxx-mini:
               diff=maxx-mini
               ans=[mini,maxx]
           if c+1>=len(numbers[r]):
               break
           num=numbers[r][c+1]
           maxx=max(maxx,num)
           heapq.heappush(minheap,(num,r,c+1))
       return ans

N = 5, K = 3
numbers[][] = {{1 3 5 7 9},
                    {0 2 4 6 8},
                    {2 3 5 7 11}}


############################################################# ----  2nd APPROACH  ----  ####################################################################


from queue import PriorityQueue
from sys import maxsize

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        q=PriorityQueue()
        maxx=-maxsize
        range_min=maxsize
        ans=[0]*2
        for i in range(len(nums)):
            #print(a[i][0])
            q.put((nums[i][0],i,0))
            if nums[i][0]>maxx:
                maxx=nums[i][0]
            
        while not q.empty():
            mini=q.get()
            if maxx-mini[0]<range_min:
                range_min=maxx-mini[0]
                ans[0]=mini[0]
                ans[1]=maxx
            if mini[2]<len(nums[mini[1]])-1:
                i=mini[1]
                j=mini[2]+1
                q.put((nums[i][j],i,j))
                if nums[i][j]>maxx:
                    maxx=nums[i][j]
            else:
                return ans 
            
Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]