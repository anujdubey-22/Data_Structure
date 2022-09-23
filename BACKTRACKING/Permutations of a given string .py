'''
Expected Time Complexity: O(n! * n)
Expected Space Complexity: O(n)
'''


class Solution:
    def swap(self,s,i,j):
        if i==j:
            return s
        return (s[:i]+s[j]+s[i+1:j]+s[i]+s[j+1:])
    def solve(self,s,ind,n):
        global ans 
        if ind>=n:
            ans.append(s)
        for i in range(ind,n):
            s=self.swap(s,ind,i)
            self.solve(s,ind+1,n)
            s=self.swap(s,ind,i)
    def find_permutation(self, S):
        # Code here
        global ans 
        ans=[]
        self.solve(S,0,len(S))
        ans.sort()
        return ans
