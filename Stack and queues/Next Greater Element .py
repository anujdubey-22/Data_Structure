'''
Expected Time Complexity : O(N). ( the element will be pop after it is pushed in stack that is why the T.C :O(N) )
Expected Auxilliary Space : O(N)
'''

class Solution:
    def nextLargerElement(self,arr,n):
        #code here
        stack=[]
        stack.append(arr[n-1])
        ans=[-1]*n
        for i in range(n-2,-1,-1): # iterating from 2nd last element (right to left)
            while len(stack)>0 and arr[i]>=stack[-1]:   # pop from stack untill the element in stack is smaller than array .
                stack.pop()  # In this way we only got the greater element in stack and thus is the answer for the previous element
                # if we got the element greater than array[i] while performing pop operation.Then this greater element is the ans for array[i] 
            
            if len(stack)!=0:
                ans[i]=stack[-1]
            else:
                ans[i]=-1
            stack.append(arr[i])
        return ans
