'''
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(K)
'''

def solve(a,k):
    n=len(a)
    q=[]
    ans=[]
    for i in range(k):
        if a[i]<0:
            q.append(a[i])
            
    for i in range(k,n):
        if len(q)>0:
            ans.append(q[0])
            if a[i-k]==q[0]:
                q.pop(0)
            
            
        else:
            ans.append(0)
        if a[i]<0:
                q.append(a[i])
            
    if len(q)>0:
        ans.append(q[0])
    else:
        ans.append(0)
    return ans 
        




a=[12, -1, -7, 8, -15, 30, 16, 28]
print(solve(a,3))
