'''
Expected Time Complexity: O(V+E).
Expected Auxiliary Space: O(V).
'''
######################     Kosaraju's Algo     ################################################################
'''
1. DFS + Stack + visited
2. reverse the graph
3. start DFS from stack elements one by one and increase count on every DFS called in main function .

'''

from collections import defaultdict
import sys
sys.setrecursionlimit(10^7)
class Solution:
    
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        def strongConnection(node,V,g):
            vis[node]=1
            for vertex in g[node]:
                if vis[vertex]!=1:
                    strongConnection(vertex,V,g)
            
        def reverseGraph(V,adj):
            g=defaultdict(list)
            
            for i in range(V):
                for vertex in adj[i]:
                    g[vertex]+=[i]
                    
            return g
        
        def dfs(i,vis,stack):
            vis[i]=1
            for vertex in adj[i]:
                if vis[vertex]!=1:
                    dfs(vertex,vis,stack)
            stack.append(i)
            
        # code here
        vis=[0]*V
        stack=[]
        
        for i in range(V):
            if vis[i]!=1:
                dfs(i,vis,stack)
                
        g=reverseGraph(V,adj)
        count=0
        vis=[0]*V
        for i in range(len(stack)):
            node=stack.pop()
            if vis[node]!=1:
                count+=1  ########### increase the count on every DFS called .
                strongConnection(node,V,g)
        
        return count