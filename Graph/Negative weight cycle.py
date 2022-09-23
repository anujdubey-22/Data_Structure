'''
Expected Time Complexity: O(n*m)
Expected Space Compelxity: O(n)
'''
# little different from Dijkstra algorithm.
import sys
class Solution:
	def isNegativeWeightCycle(self, n, edges):
		#Code here
		dist=[sys.maxsize]*n
		dist[0]=0
		
		for i in range(0,n-1):
		    for j in range(0,len(edges)):
		        u,v,weight=edges[j]
		        if dist[v]>dist[u]+weight:
		            dist[v]=dist[u]+weight
		            
		            
	    for i in range(0,len(edges)): # one more iteration to check if negetive cycle contains or not . if further distance will be relaxed then it contains cycle .
	        u,v,weight=edges[i]
	        if dist[v]>dist[u]+weight:
	            return 1
	            
	    return 0