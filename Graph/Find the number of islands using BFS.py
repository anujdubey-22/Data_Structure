'''
Expected Time Compelxity: O(n*m)
Expected Space Compelxity: O(n*m)
'''

class Solution:
    def numIslands(self,grid):
        #code here
        row=len(grid)
        col=len(grid[0])
        q=[]
        island=0
        for x in range(0,row):
            for y in range(0,col):
                
                if grid[x][y]==1:
                    island+=1
                    grid[x][y]=0
                    q.append([x,y])
                    
                while len(q)>0:
                    i,j=q.pop(0)
                    
                    if i-1>=0 and j-1>=0 and grid[i-1][j-1]==1:
                        grid[i-1][j-1]=0
                        q.append([i-1,j-1])
                    if i-1>=0 and j<col and grid[i-1][j]==1:
                        grid[i-1][j]=0
                        q.append([i-1,j])
                    if i-1>=0 and j+1<col and grid[i-1][j+1]==1:
                        grid[i-1][j+1]=0
                        q.append([i-1,j+1])
                    if i<row and j-1>=0 and grid[i][j-1]==1:
                        grid[i][j-1]=0
                        q.append([i,j-1])
                    if i<row and j+1<col and grid[i][j+1]==1:
                        grid[i][j+1]=0
                        q.append([i,j+1])
                    if i+1<row and j-1>=0 and grid[i+1][j-1]==1:
                        grid[i+1][j-1]=0
                        q.append([i+1,j-1])
                    if i+1<row and j<col and grid[i+1][j]==1:
                        grid[i+1][j]=0
                        q.append([i+1,j])
                    if i+1<row and j+1<col and grid[i+1][j+1]==1:
                        grid[i+1][j+1]=0
                        q.append([i+1,j+1])
        return island