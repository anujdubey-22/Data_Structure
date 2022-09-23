'''
Time Complexity: O(n)
'''

def solve(a,k):
    n=len(a)
    small=[]
    ans_small=[]
    big=[]
    ans_big=[]
    summ=0
    
    for i in range(k):
        while len(small)>0 and small[-1]>a[i]:
            small.pop(-1)
        small.append(a[i])
        
        while len(big)>0 and big[-1]<a[i]:
            big.pop(0)
        big.append(a[i])
        
    for i in range(k,n):
        
        summ+=small[0]+big[0]
        
        if a[i]==small[0]:
            small.pop(0)
            
        if a[i]==big[0]:
            big.pop(0)
            
        while len(small)>0 and small[-1]>a[i]:
            small.pop(-1)
        small.append(a[i])
        
        while len(big)>0 and big[-1]<a[i]:
            big.append(a[i])
        big.append(a[i])
    
    summ+=small[0]+big[0]
    
    return summ


arr=[2, 5, -1, 7, -3, -1, -2]
k=4
print(solve(arr,k))