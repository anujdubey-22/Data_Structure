'''
Expected Time Complexity: O(4^(n^2)) ---> 4 ki power n square
Expected Space Complexity: O(N^2)
'''


def solve(mat,x,y,r,c,i,j,vis,count):
    global max
    if x<0 or y<0 or x>=r or y>=c :
        return 
    if x==i and y==j:
        if max<count:
            max=count
        return
    

    if mat[x][y]!=0:
        if vis[x][y]!=1:
            vis[x][y]=1
            solve(mat,x-1,y,r,c,i,j,vis,count+1)
            solve(mat,x,y+1,r,c,i,j,vis,count+1)
            solve(mat,x,y-1,r,c,i,j,vis,count+1)
            solve(mat,x+1,y,r,c,i,j,vis,count+1)
            vis[x][y]=0
        return
    return

            



mat = [[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 0, 1, 1, 0, 1, 1, 0, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] ]
    
r=len(mat)
c=len(mat[0])
global max
max=-999999999
count=0

vis=[[0 for i in range(c)]for j in range(r)]

solve(mat,0,0,r,c,1,7,vis,count)
print(max)

################################################################################################################3


'''
Expected Time Complexity: O(4^(n^2)) ---> 4 ki power n square
Expected Space Complexity: 1

'''

def solve(mat,x,y,r,c,i,j,count):
    global max
    if x<0 or y<0 or x>=r or y>=c :
        return 
    if x==i and y==j:
        if max<count:
            max=count
        return
    

    if mat[x][y]!=0:
        #if vis[x][y]!=1:
        mat[x][y]=0
        solve(mat,x-1,y,r,c,i,j,count+1)
        solve(mat,x,y+1,r,c,i,j,count+1)
        solve(mat,x,y-1,r,c,i,j,count+1)
        solve(mat,x+1,y,r,c,i,j,count+1)
        mat[x][y]=1
        #return
    return

            

mat = [[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 0, 1, 1, 0, 1, 1, 0, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] ]
    
r=len(mat)
c=len(mat[0])
global max
max=-999999999
count=0

solve(mat,0,0,r,c,1,7,count)
print(max)