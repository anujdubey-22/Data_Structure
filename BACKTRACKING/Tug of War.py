'''
    Time Complexity: O(2^n)
'''

import sys
def solve(ind,arr,s1,s2,sum1,sum2):
    global mini,ans
    if ind>=len(arr):
        diff=abs(sum1-sum2)
        if mini>diff:
            mini=diff
            ans=str(s1)+" "+str(s2)
            
        return 
    
    if len(s1)<(len(arr)+1)//2:
        s1.append(arr[ind])
        solve(ind+1,arr,s1,s2,sum1+arr[ind],sum2)
        s1.pop()
        
    if len(s2)<(len(arr)+1)//2:
        s2.append(arr[ind])
        solve(ind+1,arr,s1,s2,sum1,sum2+arr[ind])
        s2.pop()
    
arr=[23, 45, -34, 12, 0, 98, -99, 4, 189, -1, 4]
global mini
ans=""
s1,s2=[],[]

mini=sys.maxsize
sum1,sum2=0,0
solve(0,arr,s1,s2,sum1,sum2)
print(ans)