'''
Constraints:

    m == mat.length
    n == mat[i].length
    1 <= m, n <= 104
    1 <= m * n <= 104
    mat[i][j] is either 0 or 1.
    There is at least one 0 in mat.
'''

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row =len(mat)
        col=len(mat[0])
        q=[]
        for i in range(0,row):
            for j in range(0,col):
                if mat[i][j]==0:
                    q.append([i,j])
                elif mat[i][j]==1:
                    mat[i][j]=-1
                    
                    
        while len(q)>0:
            value=q.pop(0)
            x=value[0]
            y=value[1]
            
            if x-1>=0 and mat[x-1][y]==-1:
                mat[x-1][y]=1+mat[x][y]
                q.append([x-1,y])
                
            if x+1<row and mat[x+1][y]==-1:
                mat[x+1][y]=1+mat[x][y]
                q.append([x+1,y])
            
            if y-1>=0 and mat[x][y-1]==-1:
                mat[x][y-1]=1+mat[x][y]
                q.append([x,y-1])
                
            if y+1<col and mat[x][y+1]==-1:
                mat[x][y+1]=1+mat[x][y]
                q.append([x,y+1])
                
        return mat