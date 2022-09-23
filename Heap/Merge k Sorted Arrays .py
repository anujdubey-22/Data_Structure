'''
Expected Time Complexity: O(K2*Log(K))
Expected Auxiliary Space: O(K)
'''

class Solution:
    #Function to merge k sorted arrays.
    def mergeKArrays(self, arr, K):
        # code here
        # return merged list
        ans=[]
        for i in range(len(arr)):
            ans+=arr[i]
            
        ans.sort()
        
        return ans
        