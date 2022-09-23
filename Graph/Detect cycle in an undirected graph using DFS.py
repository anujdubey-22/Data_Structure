'''
Expected Time Complexity: O(V + E)
Expected Space Complexity: O(V)
'''

class Solution:
    def dfs(self,node,parent_node,V,adj,vis):
        vis[node]=1
        
        for vertex in adj[node]:
            if vis[vertex]!=1:
                if self.dfs(vertex,node,V,adj,vis)==True:
                    return True
            elif vertex!=parent_node:
                return True
                
        return False
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V, adj):
	    
		#Code here
		vis=[0]*(V)
		
		for i in range(V):
		    if vis[i]!=1:
		        if self.dfs(i,-1,V,adj,vis)==True:
		            return True
	    return False
	    