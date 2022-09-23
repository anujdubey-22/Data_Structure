'''
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(k)
'''

def solve(a,k):
    n=len(a)
    q=[]
    ans=[]
    
    for i in range(k):
        while len(q)>0 and q[-1]>a[i]:
            q.pop(-1)
        q.append(a[i])
    for i in range(k,n):
        ans.append(q[0])
        
        if a[i]==q[0]:
            q.pop(0)
            
        while len(q)>0 and q[-1]>a[i]:
            q.pop(-1)
            
        q.append(a[i])
    ans.append(q[0])
    return ans


arr=[2, 5, -1, 7, -3, -1, -2]
k=3
print(solve(arr,k))