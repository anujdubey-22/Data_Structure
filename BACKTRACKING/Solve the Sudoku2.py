class Solution:
    def checkgrid(self,grid,x,y,char):
        for i in range(0,len(grid)):
            
            if grid[x][i]==char:
                return False
            if grid[i][y]==char:
                return False
                
            if grid[3*(x//3)+i//3][3*(y//3)+i%3]==char:
                return False
                
        return True
    
    #Function to find a solved Sudoku. 
    def SolveSudoku(self,grid):
    #Function to print grids of the Sudoku.   
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                
                if grid[i][j]==0:
                    
                    for char in range(1,10):
                        if self.checkgrid(grid,i,j,char):
                            grid[i][j]=char
                            if self.SolveSudoku(grid)==True:
                                return True
                            else:         # Backtrack only when solution does'not found
                                grid[i][j]=0
                            
                    return False    # This returns FALSE when above statement does'not return TRUE
        return True       # This returns TRUE when no empty space is left in sudoku
        
    def printGrid(self,arr):
        # Your code here
        for i in range(0,len(arr)):
            for j in range(0,len(arr[0])):
                print(arr[i][j],end=" ")
        
