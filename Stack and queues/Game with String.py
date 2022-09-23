'''
Expected Time Complexity: O(N*logN)  where N is the length of string
Expected Auxiliary Space: O(N)
'''

import heapq
def solve(s,k):
    heap=[]
    d={}
    summ=0
    
    for i in range(len(s)):
        if s[i] in d:
            d[s[i]]+=1
        else:
            d[s[i]]=1
            
    for values in d.values():
        heap.append(values)
        
    while k>0:
        heap.sort()
        element=heap.pop(-1)
        element-=1
        k-=1
        heap.append(element)
        
    for i in range(len(heap)):
        summ+=(heap[i]*heap[i])
        
    return summ
    
s = 'aabcbcbcabcc'
k = 8
print(solve(s,k))