'''
Expected Time Complexity: O(V + E)
Expected Space Complexity: O(V)
'''
'''
check whether the graph is colored by only 2 colors .
similar to the m-coloring problem. 
'''
############################### BFS Approach used ###############################################################

class Solution:
	def isBipartite(self, V, adj):
		#code here
		
		color=[-1]*V
        q=[]
        
        for i in range(V):
            if color[i]==-1:
                q.append(i)
                color[i]=0
                while len(q)>0:
                    node=q.pop(0)
                    
                    for vertex in adj[node]:
                        if color[vertex]==-1:
                            color[vertex]=color[node]^1 # color eighter 1 or 0 (1 XOR 1 =0  , 0 XOR 1 =1)
                            q.append(vertex)
                        elif color[vertex]==color[node]:
                            return False
                            
        return True