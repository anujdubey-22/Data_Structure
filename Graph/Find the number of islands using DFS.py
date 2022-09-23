'''
Expected Time Compelxity: O(n*m)
Expected Space Compelxity: O(n*m)
'''

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7) # important to set recursion limit

class Solution:
    def dfs(self,x,y,grid,row,col):
        if x<0 or y<0 or x>=row or y>=col or grid[x][y]==0:
            return 
        
        grid[x][y]=0
        self.dfs(x-1,y-1,grid,row,col)
        self.dfs(x-1,y,grid,row,col)
        self.dfs(x-1,y+1,grid,row,col)
        self.dfs(x,y-1,grid,row,col)
        self.dfs(x,y+1,grid,row,col)
        self.dfs(x+1,y-1,grid,row,col)
        self.dfs(x+1,y,grid,row,col)
        self.dfs(x+1,y+1,grid,row,col)
        return 
        
    def numIslands(self,grid):
        #code here
        row=len(grid)
        col=len(grid[0])
        islands=0
        for i in range(0,row):
            for j in range(0,col):
                if grid[i][j]==1:
                    islands+=1
                    self.dfs(i,j,grid,row,col)
                    
        return islands