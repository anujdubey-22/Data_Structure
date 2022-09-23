'''
Time Complexity: O(R*(2^(R*C)))
'''

def safe(mat,r,c,x,y):
    if (x==0 and y==0) :
        if mat[x][y+1]==0 or mat[x+1][y]==0:
            return False
    elif (x==r-1 and y==0):
        if mat[x][y+1]==0 or mat[x-1][y]==0:
            return False
    elif x==0 and y>0:
        if mat[x][y+1]==0 or mat[x+1][y]==0 or mat[x][y-1]==0:
            return False
    elif x>0 and y==0:
        if mat[x][y+1]==0 or mat[x+1][y]==0 or mat[x-1][y]==0:
            return False
    elif x==(r-1) and y>0:
        if mat[x][y-1]==0 or mat[x][y+1]==0 or mat[x-1][y]==0:
            return False
    elif x>0 and y>0:
        if mat[x][y+1]==0 or mat[x+1][y]==0 or mat[x][y-1]==0 or mat[x-1][y]==0:
            return False
    return True
    
def solve(mat,r,c,x,y,count):
    global mini
    if x>=r:
        return 
    if y==c-1:
        count+=1
        if mini>count:
            mini=count
        return True
    if safe(mat,r,c,x,y):
        num=mat[x][y]
        #mat[x][y]="X"
        if solve(mat,r,c,x,y+1,count+1)==True:
            return True
        #else :
        #    mat[x][y]=num
        
        #mat[x][y]="X"
        if solve(mat,r,c,x+1,y,count+1)==True:
            return True
        #else:
        #    mat[x][y]=num
    return     



def fun(mat,r,c,count):
    
    for i in range(r):
        solve(mat,r,c,i,0,count)



mat = [
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 0, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 0, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 0, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 1, 0, 1, 1, 1, 1 ],
        [ 1, 0, 1, 1, 1, 1, 1, 1, 0, 1 ],
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 0, 1, 1, 1, 1, 0, 1, 1, 1, 1 ],
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
        [ 1, 1, 1, 0, 1, 1, 1, 1, 1, 1 ]
         ]
        
r=len(mat)
global mini
mini=99999999
c=len(mat[0])
count=0
fun(mat,r,c,count)
print(mini-1)
#for i in range(r):
#    for j in range(c):
#        print(mat[i][j],end=" ")
#        
#    print()