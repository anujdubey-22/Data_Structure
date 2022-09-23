'''
Do it in-place.

Expected Time Complexity: O(n3)
Expected Space Compelxity: O(1)
'''

import sys
class Solution:
	def shortest_distance(self, matrix):
		#Code here
		n=len(matrix)
		
		for i in range(0,n):
		    for j in range(0,n):
		        if matrix[i][j]==-1:
		            matrix[i][j]=sys.maxsize
		        
		        
		for k in range(0,n):
		    for i in range(0,n):
		        for j in range(0,n):
		            matrix[i][j]=min(matrix[i][j],matrix[i][k]+matrix[k][j])
		                
	    for i in range(0,n):
		    for j in range(0,n):
		        if matrix[i][j]==sys.maxsize:
		            matrix[i][j]=-1
		                    
	    return matrix

		################################################################ 2nd Approach ###################################333

class Solution:
	def shortest_distance(self, matrix):
		#Code here
		n=len(matrix)
		
		for k in range(0,n):
		    for i in range(0,n):
		        for j in range(0,n):
		            if matrix[i][k]==-1 or matrix[k][j]==-1:
		                continue
		            if matrix[i][j]!=-1:
		                matrix[i][j]=min(matrix[i][j],matrix[i][k]+matrix[k][j])
		                
		            else:
		                if matrix[i][k]+matrix[k][j]>0:
		                    matrix[i][j]=matrix[i][k]+matrix[k][j]
		                    
		                    
	    return matrix
		