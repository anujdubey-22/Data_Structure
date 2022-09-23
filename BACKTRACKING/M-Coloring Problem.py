'''
Expected Time Complexity: O(M^N).
Expected Auxiliary Space: O(N).
'''
'''
we can also return colors array which contains which node is coloured by which color
'''
#Function to determine if graph can be coloured with at most M colours such
#that no two adjacent vertices of graph are coloured with same colour.
def check(node,graph,k,V,colors,col_to_fill):
    for i in range(V):
        if graph[node][i]==1 and colors[i]==col_to_fill:
            return False
            
    return True
    
def solve(node,graph,k,V,colors):
    if node==V:
        return True
        
    for col in range(1,k+1):
        if (check(node,graph,k,V,colors,col))==True:
            colors[node]=col
            if (solve(node+1,graph,k,V,colors))==True:
                return True
            else:
                colors[node]=0
    return False
    
def graphColoring(graph, k, V):
    
    #your code here
    colors=[0]*V
    return solve(0,graph,k,V,colors)
