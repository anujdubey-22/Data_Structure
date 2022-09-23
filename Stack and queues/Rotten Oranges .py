def rotten_oranges(matrix):
    row=len(matrix)
    col=len(matrix[0])
    time=0
    count=0
    count_0=0
    q=[]

    for i in range(0,row):
        for j in range(0,col):
            if matrix[i][j]==2:
                q.append([i,j])
                count+=1
            if matrix[i][j]==0:
                count_0+=1

    while len(q)>0:
        increment=False
        n=len(q)
        ind_x=[0,0,1,-1]
        ind_y=[-1,1,0,0]
        for i in range(0,n):
            value=q.pop(0)
            x=value[0]
            y=value[1]

            for i in range(0,4):
                nx=x+ind_x[i]
                ny=y+ind_y[i]

                if nx>=0 and nx<row and ny>=0 and ny<col and matrix[nx][ny]==1:
                    matrix[nx][ny]=2
                    q.append([nx,ny])
                    count+=1
                    increment=True

        if increment==True:
            time+=1

    if (row*col)-count_0==count:
        return time
    else:
        return -1

matrix = [[0,1,2],
[0,1,2],[2,1,1]]

print(rotten_oranges(matrix))


############################ OR ##################################

class Solution:

    #Function to find minimum time required to rot all oranges. 
	def orangesRotting(self, matrix):
		#Code here
		row=len(matrix)
        col=len(matrix[0])
        time=0
        count=0
        count_0=0
        q=[]
    
        for i in range(0,row):
            for j in range(0,col):
                if matrix[i][j]==2:
                    q.append([i,j])
                    count+=1
                if matrix[i][j]==0:
                    count_0+=1
    
        while len(q)>0:
            n=len(q)
            
            for i in range(0,n):
                value=q.pop(0)
                x=value[0]
                y=value[1]
    
                if x-1>=0 and matrix[x-1][y]==1:
                    matrix[x-1][y]=2
                    q.append([x-1,y])
                    count+=1
                if x+1<row and matrix[x+1][y]==1:
                    matrix[x+1][y]=2
                    q.append([x+1,y])
                    count+=1
                if y+1<col and matrix[x][y+1]==1:
                    matrix[x][y+1]=2
                    q.append([x,y+1])
                    count+=1
                if y-1>=0 and matrix[x][y-1]==1:
                    matrix[x][y-1]=2
                    q.append([x,y-1])
                    count+=1
                
            if len(q)>0:
                time+=1
    
        if (row*col)-count_0==count:
            return time
        else:
            return -1


#{ 
#  Driver Code Starts
from queue import Queue

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.orangesRotting(grid)
		print(ans)

# } Driver Code Ends