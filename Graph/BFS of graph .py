'''
Given a directed graph. The task is to do Breadth First Traversal of this graph starting from 0.
'''

'''
Expected Time Complexity: O(V + E)
Expected Auxiliary Space: O(V)
'''

class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        # code here
        q=[]
        q.append(0)
        vis=[0]*(V+1)
        vis[0]=1
        ans=[]
        
        while len(q)>0:
            node=q.pop(0)
            ans.append(node)
            
            for i in adj[node]:
                if vis[i]!=1:
                    q.append(i)
                    vis[i]=1
                    
        return ans 
        