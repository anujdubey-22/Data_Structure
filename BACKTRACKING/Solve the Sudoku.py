class Solution:
    def checkgrid(self,grid,x,y,position):
        for j in range(9):
            if grid[x][j]==position:
                return False
        for i in range(9):
            if grid[i][y]==position:
                return False
                
        sub_mat_i=x//3*3
        sub_mat_j=y//3*3
        for i in range(0,3):
           for j in range(0,3):
               if grid[sub_mat_i+i][sub_mat_j+j]==position:
                   return False
        return True
        
    def solve(self,grid,i,j):
        global flag,ans
        
        if i==len(grid):
            ans.append(grid)
            flag=True
            return True
        
        ni=i
        nj=j
        
        if j==len(grid)-1:
            ni=i+1
            nj=0
        else:
            ni=i
            nj=j+1
            
        if grid[i][j]!=0:
            self.solve(grid,ni,nj)
        else:
            for position in range(1,10):
                if self.checkgrid(grid,i,j,position):
                    grid[i][j]=position
                    if (self.solve(grid,ni,nj)):
                        return True
                    grid[i][j]=0
        
    #Function to find a solved Sudoku. 
    def SolveSudoku(self,grid):
        global flag,ans
        ans=[]
        flag=False
        self.solve(grid,0,0)
        return flag
    
    #Function to print grids of the Sudoku.    
    def printGrid(self,arr):
        # Your code here
        global ans 
        arr=ans
        print(arr,"arr")
        #for i in range(0,9):
        #    for j in range(0,9):
        #        print(arr[i][j],end=" ")
