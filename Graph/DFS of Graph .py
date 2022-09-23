'''
Note: Use recursive approach to find the DFS traversal of the graph starting from the 0th vertex
Expected Time Complexity: O(V + E)
Expected Auxiliary Space: O(V) 
'''

class Solution:
    def solve(self,V,adj,vis,stack,node):
        stack.append(node)
        vis[node]=1
        for i in adj[node]:
            if vis[i]!=1:
                self.solve(V,adj,vis,stack,i)
        
        
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        stack=[]
        vis=[0]*(V+1)
        self.solve(V,adj,vis,stack,0)
        return stack
