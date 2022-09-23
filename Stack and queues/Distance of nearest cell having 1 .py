'''
Expected Time Complexity: O(n*m)
Expected Auxiliary Space: O(n*m)
'''

def solve(m):
    row=len(m)
    col=len(m[0])
    q=[]
    for i in range(0,row):
        for j in range(0,col):
            if m[i][j]==1:
                m[i][j]=0
                q.append([i,j])
            elif m[i][j]==0:
                m[i][j]=-1
                
    while len(q)>0:
        value=q.pop(0)
        x=value[0]
        y=value[1]
        
        if x-1>=0 and m[x-1][y]==-1:
            m[x-1][y]=m[x][y]+1
            q.append([x-1,y])
        
        if x+1<row and m[x+1][y]==-1:
            m[x+1][y]=m[x][y]+1
            q.append([x+1,y])
            
        if y-1>=0 and m[x][y-1]==-1:
            m[x][y-1]=m[x][y]+1
            q.append([x,y-1])
        
        if y+1<col and m[x][y+1]==-1:
            m[x][y+1]=m[x][y]+1
            q.append([x,y+1])
            
    return m        
    



grid = [[1,0,0,1],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0]]
solve(grid)
print(grid)
