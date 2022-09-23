'''
Time Complexity: O(N)   
'''

def solve(a):
    n=len(a)
    ans=[-1]*n
    stack=[]
    stack.append(a[n-1])
    for i in range(n-2,-1,-1):
        if a[i]<stack[-1]:
            ans[i]=stack[-1]
        else:
            while len(stack)>0 and stack[-1]<a[i]:
                stack.pop()
            if len(stack)>0:
                ans[i]=stack[-1]
        stack.append(a[i])
    return ans
a=[11, 13, 21, 3]
print(solve(a))