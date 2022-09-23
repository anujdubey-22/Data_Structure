'''
Expected Time Complexity: O(V + E)
Expected Space Complexity: O(V)
'''

class Solution:
    
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V, adj):
		#Code here
		vis=[0]*(V)
		parent_node=[0]*(V)
		q=[]
		
		for vertex in range(V):
		    if vis[vertex]!=1:
		        q.append(vertex)
		        vis[vertex]=1
		        while len(q)>0:
		            node=q.pop(0)
		            for i in adj[node]:
		                
		                if vis[i]!=1:
		                    vis[i]=1
		                    q.append(i)
		                    parent_node[i]=node
		                    
	                    elif parent_node[node]!=i:
	                        return True
	    return False
	    