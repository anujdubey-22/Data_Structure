'''
Expected Time Complexity: O(X2 * 2N), where X is average of summation B/arri for every number in the array.
Expected Auxiliary Space: O(X * 2N)
'''
class Solution:
    def solve(self,ind,arr,summ,s,output,n,ans):
        if ind>=n or s>summ:
            return 
        if s==summ:
            #output=output[:-1]
            #if output not in ans:
            ans.append(list(output))  ## ----->  IMPORTANT STEPS TO ADD INTO ANS ARRAY 
            return 
        output.append(arr[ind])
        self.solve(ind,arr,summ,s+arr[ind],output,n,ans)
        output.pop()
        self.solve(ind+1,arr,summ,s,output,n,ans)
        
    #Function to return a list of indexes denoting the required 
    #combinations whose sum is equal to given number.
    def combinationalSum(self,A, B):
    # A is array and   B is sum 
        # code here
        s=set()
        for i in range(len(A)):
            if A[i] not in s:
                s.add(A[i])
                
        n=len(s)
        arr=[0]*n
        for i in range(n):
            arr[i]=s.pop()
        arr.sort()
        #global ans
        ans=[]
        output=[]
        s=0
        #n=len(A)
        self.solve(0,arr,B,s,output,n,ans)
        return ans 
