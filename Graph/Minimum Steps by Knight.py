'''
Expected Time Complexity: O(N2).
Expected Auxiliary Space: O(N2).
'''

class Solution:
    def solve(self,n,x1,x2,y1,y2):
        vis=[[-1 for i in range(n)] for i in range(n)]
        q=[]
        q.append([x1,y1])
        vis[x1][y1]=0
        while len(q)>0:
            i,j=q.pop(0)
            
            if i==x2 and j==y2 :
                return (vis[i][j])
            
            if i-2>=0 and j-1>=0 and vis[i-2][j-1]==-1:
                vis[i-2][j-1]=vis[i][j]+1
                q.append([i-2,j-1])
                
            if i-1>=0 and j-2>=0 and vis[i-1][j-2]==-1:
                vis[i-1][j-2]=vis[i][j]+1
                q.append([i-1,j-2])
                
            if i-1>=0 and j+2<n and vis[i-1][j+2]==-1:
                vis[i-1][j+2]=vis[i][j]+1
                q.append([i-1,j+2])
            
            if i-2>=0 and j+1<n and vis[i-2][j+1]==-1:
                vis[i-2][j+1]=vis[i][j]+1
                q.append([i-2,j+1])
                
            if i+2<n and j+1<n and vis[i+2][j+1]==-1:
                vis[i+2][j+1]=vis[i][j]+1
                q.append([i+2,j+1])
                
            if i+1<n and j+2<n and vis[i+1][j+2]==-1:
                vis[i+1][j+2]=vis[i][j]+1
                q.append([i+1,j+2])
                
            if i+2<n and j-1>=0 and vis[i+2][j-1]==-1:
                vis[i+2][j-1]=vis[i][j]+1
                q.append([i+2,j-1])
            
            if i+1<n and j-2>=0 and vis[i+1][j-2]==-1:
                vis[i+1][j-2]=vis[i][j]+1
                q.append([i+1,j-2])
    
	#Function to find out minimum steps Knight needs to reach target position.
	def minStepToReachTarget(self, KnightPos, TargetPos, N):
		#Code here
		x1=KnightPos[0]-1
        y1=KnightPos[1]-1
        x2=TargetPos[0]-1
        y2=TargetPos[1]-1
        
        return (self.solve(N,x1,x2,y1,y2))