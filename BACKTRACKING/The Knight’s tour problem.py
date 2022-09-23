def printchess(chess):
    for i in range(n):
        for j in range(n):
            print(chess[i][j],end=" ")
            
        print()
    return 
def safe(chess,n,r,c):
    if chess[r][c]!=-1:
        return False
    return True
    
def solve(chess,n,r,c,move):
    if r<0 or c<0 or r>=n or c>=n or chess[r][c]!=-1:
        return 
    if move==(n*n)-1:
        chess[r][c]=move
        printchess(chess)
        return True
    #if safe(chess,n,r,c):
    chess[r][c]=move
    if solve(chess,n,r+2,c+1,move+1):
        return True
    if solve(chess,n,r+1,c+2,move+1):
        return True
    if solve(chess,n,r-1,c+2,move+1):
        return True
    if solve(chess,n,r-2,c+1,move+1):
        return True
    if solve(chess,n,r-2,c-1,move+1):
        return True
    if solve(chess,n,r-1,c-2,move+1):
        return True
    if solve(chess,n,r+1,c-2,move+1):
        return True
    if solve(chess,n,r+2,c-1,move+1):
        return True
    chess[r][c]=-1
    return 

n=8
chess=[[-1 for i in range(n)]for j in range(8)]

solve(chess,n,0,0,0)