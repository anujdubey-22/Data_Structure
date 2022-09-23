'''
Expected Time Complexity: O(V2).
Expected Auxiliary Space: O(V2).
'''

import sys
from queue import PriorityQueue

class Solution:
    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        vis=[0]*V
        dis=[sys.maxsize]*V
        q=PriorityQueue()
        q.put((0,S))
        dis[S]=0
        while not q.empty():
            node_dis,node=q.get()
            vis[node]=1
            
            for vertex ,weight in adj[node]:
                if dis[vertex]>node_dis+weight and vis[vertex]==0:
                    dis[vertex]=node_dis+weight
                    q.put((dis[vertex],vertex))
        return dis
        
