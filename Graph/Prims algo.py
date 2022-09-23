'''
Expected Time Complexity: O(ElogV).
Expected Auxiliary Space: O(V2).
'''

from queue import PriorityQueue
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        q=PriorityQueue()
        vis=[0]*V
        ans=0
        q.put((0,0))
        
        while not q.empty():
            weight,node=q.get()
            if vis[node]==1:
                continue
            vis[node]=1
            ans+=weight
            
            for vertex,vertex_weight in adj[node]:
                if vis[vertex]!=1:
                    
                    q.put((vertex_weight,vertex))
                    
        return ans 