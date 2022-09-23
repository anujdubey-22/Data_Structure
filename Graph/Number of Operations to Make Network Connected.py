
class Solution:
    def dfs(self,graph,vis,node):
        vis[node]=1
        if not node in graph: # if the node is not present in graph this means ,that specific node has no adjacency list therefor return from here 
            return 
        list=graph[node]
        for vertex in list:
            if vis[vertex]!=1:
                self.dfs(graph,vis,vertex)
                
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        edges=len(connections)
        if edges<n-1:
            return -1
        graph={}                 # for creating our own adjacency list
        for u,v in connections:   #creating adjacency list
            if u in graph:
                graph[u]+=[v]
            else:
                graph[u]=[v]
            if v in graph:
                graph[v]+=[u]
            else:
                graph[v]=[u]
        
        vis=[0]*n
        count=0   # for counting the components of the graph
        for i in range(n):
            if vis[i]!=1:
                count+=1
                self.dfs(graph,vis,i)
                                    
        return count-1
        