'''
Expected Time Complexity: O(V + E)
Expected Auxiliary Space: O(V) 
'''

class Solution:
    def solve(self,node,vis,recStack,adj):
        vis[node]=1
        recStack[node]=1
        
        for vertex in adj[node]:
            if vis[vertex]!=1:
                if self.solve(vertex,vis,recStack,adj)==True:
                    return True
            else:
                if recStack[vertex]==1:
                    return True
        recStack[node]=0
        return False
                
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        vis=[0]*(V+1)
        recStack=[0]*(V+1)
        
        for i in range(V):
            if vis[i]!=1:
                if self.solve(i,vis,recStack,adj)==True:
                    return True
                    
        return False
        