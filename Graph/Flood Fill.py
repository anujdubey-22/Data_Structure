'''
Time Complexity: row*column
'''

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m=len(image)
        n=len(image[0])
        old_color=image[sr][sc]
        vis=[[-1 for i in range(n)]for j in range(n)]
        q=[]
        q.append([sr,sc])
        image[sr][sc]=newColor
        vis[sr][sc]=newColor
        
        
        while len(q)>0:
            i,j=q.pop(0)
            
            if i-1>=0 and j<n and image[i-1][j]==old_color and vis[i-1][j]==-1:
                image[i-1][j]=newColor
                vis[i-1][j]=newColor
                q.append([i-1,j])
                
            if i<m and j-1>=0 and image[i][j-1]==old_color and vis[i][j-1]==-1:
                image[i][j-1]=newColor
                image[i][j-1]==old_color
                q.append([i,j-1])
                
            if i<m and j+1<n and image[i][j+1]==old_color and vis[i][j+1]==-1:
                image[i][j+1]=newColor
                image[i][j+1]==old_color
                q.append([i,j+1])
                
            if i+1<m and j<n and image[i+1][j]==old_color and vis[i+1][j]==-1:
                image[i+1][j]=newColor
                image[i+1][j]==old_color
                q.append([i+1,j])
                
                
        return image
    