def addEdge(u, v, w):
    adj[u].append([v, w])
    adj[v].append([u, w])
'''
Time Complexity: O(n!) 
'''


def solve(src,graph,k,vis):
    vis[src]=1
    if k<=0:
        return True
    for i in range(len(graph[src])):
        vertex=graph[src][i][0]
        weight=graph[src][i][1]
        if vis[vertex]==1:
            continue
        if weight>=k:
            return True
            
        vis[vertex]=1
        
        if solve(vertex,graph,k-weight,vis)==True:
            return True
        vis[vertex]=0
    return False
        
V = 9
#g = Graph(V)
adj = [[] for i in range(V)]
#  making above shown graph
addEdge(0, 1, 4)
addEdge(0, 7, 8)
addEdge(1, 2, 8)
addEdge(1, 7, 11)
addEdge(2, 3, 7)
addEdge(2, 8, 2)
addEdge(2, 5, 4)
addEdge(3, 4, 9)
addEdge(3, 5, 14)
addEdge(4, 5, 10)
addEdge(5, 6, 2)
addEdge(6, 7, 1)
addEdge(6, 8, 6)
addEdge(7, 8, 7)
print(adj)
src = 0
k = 62
vis=[0]*V
if solve(src,adj,k,vis)==True:
    print("True")
else:
    print("False")