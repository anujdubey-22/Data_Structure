'''
TC- O(2^(n*m))   , SC – O(n+m) 
'''
def solve(mat,x,y,r,c,output):
    global ans
    if x>=r or y>=c:
        return
    if x==r-1 and y==c-1:
        output+=str(mat[x][y])
        ans.append(output)
        return
    num=str(mat[x][y])
    solve(mat,x+1,y,r,c,output+num+" ")
    solve(mat,x,y+1,r,c,output+num+" ")
    return



mat = [[1,2,3],
            [4,5,6],
            [7,8,9]]
       
r=len(mat)
c=len(mat[0])
global ans 
ans=[]
output=""
solve(mat,0,0,r,c,output)
for i in range(len(ans)):
    for j in range(len(ans[i])):
        print(ans[i][j],end="")
        
    print()