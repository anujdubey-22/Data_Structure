'''
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(k)
'''

def printMax(arr, n, k):
    q=[]
    ans=[]
    
    for i in range(k):
        while len(q)>0 and q[-1]<arr[i]:
            q.pop(-1)
        q.append(arr[i])
        
    for i in range(k,n):
        ans.append(q[0])
        
        if arr[i-k]==q[0]:
            q.pop(0)
            
        while len(q)>0 and q[-1]<arr[i]:
            q.pop(-1)
            
        q.append(arr[i])
    ans.append(q[0])
    return ans




arr = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
k = 4
print(printMax(arr, len(arr), k))