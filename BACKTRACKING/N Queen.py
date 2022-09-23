class Solution:
    def isSafe(self,matrix,n,row,col):
        # vertical check
        for i in range(row,-1,-1):
            if matrix[i][col]==1:
                return False
                
        # left upper diagonal check
        i=row
        j=col
        while i>=0 and j>=0:
            if matrix[i][j]==1:
                return False
            i-=1
            j-=1
        
        # right upper diagonal check
        i=row
        j=col
        while i<n and j<n:
            if matrix[i][j]==1:
                return False
            i-=1
            j+=1
            
            
    def solve(self,matrix,n,row,output):
        global ans
        if row==n:
            ans.append(output)
            return 
            
        for col in range(n):
            if self.isSafe(matrix,n,row,col):
                matrix[row][col]=1
                self.solve(matrix,n,row,output+"col+1")
                matrix[row][col]=0
     
    
    def nQueen(self, n):
        # code here
        matrix=[[0 for i in range(n)]for j in range(n)]
        global ans
        ans=[]
        output=""
        self.solve(matrix,n,0,output)
        
        #ans.sort
        return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.nQueen(n)
        if(len(ans) == 0):
            print("-1")
        else:
            for i in range(len(ans)):
                print("[",end="")
                for j in range(len(ans[i])):
                    print(ans[i][j],end = " ")
                print("]",end = " ")
            print()
                
# } Driver Code Ends