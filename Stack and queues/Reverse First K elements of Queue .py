'''
Expected TIme Complexity : O(n)
Expected Auxilliary Space : O(n)
'''

def modifyQueue(q,k):
    # code here
    stack=[]
    
    count=0
    while len(q)>0 and count<k:
        stack.append(q.pop(0))
        count+=1
    while len(stack)>0:
        q.append(stack.pop())
        
    n=len(q)-k
    for i in range(n):
        q.append(q.pop(0))
    return q
    