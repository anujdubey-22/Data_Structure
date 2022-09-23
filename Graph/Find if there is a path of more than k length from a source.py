'''
by using DFS approach we can return the True or also we can return the path travelled
we can also return and find the  weight of longest path from a given source.
'''

# Program to find if there is a simple path with
# weight more than k

# This class represents a dipathted graph using
# adjacency list representation
class Graph:
	# Allocates memory for adjacency list
	def __init__(self, V):
		self.V = V
		self.adj = [[] for i in range(V)]

	# Returns true if graph has path more than k length
	def pathMoreThanK(self,src, k):
	    
	    def dfs(src,k,vis,w,st): 
	        global max_weight 
	        vis[src]=1
	        max_weight =max(max_weight,w)
	        if w>k:
	            ans.append(st)
	            return True
	        for vertex,weight in self.adj[src]:
	            if vis[vertex]!=1:
	                if dfs(vertex,k,vis,w+weight,st+' '+str(vertex))==True:
	                    return True
	                
	        vis[src]=0
	        return
	    
	    vis=[0]*V # visited array 
	    ans=[] # for storing path
	    global max_weight
	    max_weight=0 # for maximum weight travelled from source
	    st='' # for creating string of travelled path so that we can store it in array.
	    #print(self.adj)
	    dfs(src,k,vis,0,st+'0')  # call DFS function .
	    return ans,max_weight # return the path travelled and weight of longest path from a given source.
	    
	    
	    
	# Utility function to an edge (u, v) of weight w
	def addEdge(self,u, v, w):
		self.adj[u].append([v, w])
		self.adj[v].append([u, w])

# Driver program to test methods of graph class
if __name__ == '__main__':

	# create the graph given in above fugure
	V = 9
	g = Graph(V)

	# making above shown graph
	g.addEdge(0, 1, 4)
	g.addEdge(0, 7, 8)
	g.addEdge(1, 2, 8)
	g.addEdge(1, 7, 11)
	g.addEdge(2, 3, 7)
	g.addEdge(2, 8, 2)
	g.addEdge(2, 5, 4)
	g.addEdge(3, 4, 9)
	g.addEdge(3, 5, 14)
	g.addEdge(4, 5, 10)
	g.addEdge(5, 6, 2)
	g.addEdge(6, 7, 1)
	g.addEdge(6, 8, 6)
	g.addEdge(7, 8, 7)

	src = 0
	k = 58
	print(g.pathMoreThanK(src, k))
		

	k = 61
	if g.pathMoreThanK(src, k):
		print("Yes")
	else:
		print("No")
