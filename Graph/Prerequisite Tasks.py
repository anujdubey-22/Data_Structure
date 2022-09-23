'''
Expected Time Complexity: O(N + P)
Expected Auxiliary Space: O(N + P)
'''
'''
make graph(adjacency list) from prerequisites list and do topological sort.
'''

from collections import defaultdict
class Solution:
    def isPossible(self,N,prerequisites):
        #code here
        d=defaultdict(list)
        for i in range(len(prerequisites)):
            v,u=prerequisites[i]
            d[u]+=[v]
        q=[]
        in_degree=[0]*N
        for i in range(len(prerequisites)):
            in_degree[prerequisites[i][0]]+=1
            
        for i in range(len(in_degree)):
            if in_degree[i]==0:
                q.append(i)
                
        if len(q)==0:
            return False
        count=0
        while len(q)>0:
            node=q.pop(0)
            count+=1
            for vertex in d[node]:
                in_degree[vertex]-=1
                if in_degree[vertex]==0:
                    q.append(vertex)
                    
        if count==N:
            return True
        else:
            return False