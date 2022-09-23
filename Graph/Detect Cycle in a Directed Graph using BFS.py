'''
Expected Time Complexity: O(V + E)
Expected Auxiliary Space: O(V)

'''

class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        
        in_degree=[0]*V
        
        for i in range(V):
            for adjacent in adj[i]:
                in_degree[adjacent]+=1
                
        q=[]
        for i in range(V):
            if in_degree[i]==0:
                q.append(i)
        
                
        count=0
        while len(q)>0:
            node=q.pop(0)
            
            for vertex in adj[node]:
                in_degree[vertex]-=1
                if in_degree[vertex]==0:
                    q.append(vertex)
                    
            count+=1
        if count==V:
            return False
        else:
            return True
