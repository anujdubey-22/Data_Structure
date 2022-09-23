'''
Expected Time Complexity: O(n!/(n-k)!) , where n = length of input string
Expected Auxiliary Space: O(n)
'''

class Solution:
    def swap(self,s,i,j):
        if s[i]==s[j]: # if same number has to swap then return simply the string because no swap needed here.
            return s
        return (s[:i]+s[j]+s[i+1:j]+s[i]+s[j+1:])
        
    def solve(self,s,k,n,ind):
        global max
        if k==0 or ind>=n:
            return
        big=s[ind]
        for i in range(ind+1,n):
           if s[i]>big:
               big=s[i]
        if s[ind]==big:  # if no greater value is found for the current value that means no swap needed  just pass the next index for the recursion and dont decrement the (k) as no swap is done 
            self.solve(s,k,n,ind+1)
        for i in range(n-1,ind-1,-1): # if same number is present more than one than try swaping from last to first as in this way we can obtain all recursion . 
                                      # and also in general by swaping the last index greater number leads to the greater string formed .   
            if s[i]==big:             
                s=self.swap(s,ind,i)
                if max<s:
                    max=s
                self.solve(s,k-1,n,ind+1)
                s=self.swap(s,ind,i)
        
        
    #Function to find the largest number after k swaps.
    def findMaximumNum(self,s,k):
        #code here
        #arr=list(s)
        global max
        max=s
        self.solve(s,k,len(s),0)
        return max
