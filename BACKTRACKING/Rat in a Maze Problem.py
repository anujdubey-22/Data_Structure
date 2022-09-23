'''
Expected Time Complexity: O((3N^2)).
Expected Auxiliary Space: O(L * X), L = length of the path, X = number of paths.
'''

class Solution:
    def solve(self,m,n,i,j,output,visited):
        global ans
        
        if i>=n or i<0 or j>=n or j<0:
            return 
        if m[i][j]==0 or visited[i][j]==1:
            return 
        
        if i==n-1 and j==n-1:
            ans.append(output)
            return 
        
        visited[i][j]=1   # Backtracking
        
        right=self.solve(m,n,i,j+1,output+"R",visited)
        left=self.solve(m,n,i,j-1,output+"L",visited)
        down=self.solve(m,n,i+1,j,output+"D",visited)
        up=self.solve(m,n,i-1,j,output+"U",visited)
        
        visited[i][j]=0   # Backtracking
        
    def findPath(self, m, n):
        # code here
        global ans    
        ans=[]
        if m[0][0]==0 or m[n-1][n-1]==0:
            return ans
            
        
        output=""
        visited=[[0 for i in range(n)]for j  in range(n)]
        self.solve(m,n,0,0,output,visited)
        
        ans=sorted(ans)
        return ans
