'''
Expected Time Complexity: O(V + E).
Expected Auxiliary Space: O(V).
'''

class Solution:

    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        
        in_degree=[0]*V
        q=[]
        ans=[]
        for i in range(V):
            for vertex in adj[i]:
                in_degree[vertex]+=1
                
        for i in range(len(in_degree)):
            if in_degree[i]==0:
                q.append(i)
                
        while len(q)>0:
            node=q.pop(0)
            ans.append(node)
            for vertex in adj[node]:
                in_degree[vertex]-=1
                if in_degree[vertex]==0:
                    q.append(vertex)
                
        return ans