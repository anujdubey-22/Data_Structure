'''
Expected Time Complexity: O(N*N)
Expected Auxilliary Space: O(N) recursive.
'''

def sort(stack,value):
    if len(stack)==0:
        stack.append(value)
        return 
    
    if len(stack)>0:
        if len(stack)>0 and stack[-1]>value:
            ele=stack.pop()
            sort(stack,value)
            stack.append(ele)
        else:
            stack.append(value)
            
    return 
    
def solve(stack):
    if len(stack)==0:
        return 
    
    value=stack.pop()
    solve(stack)
    
    sort(stack,value)
    return 

stack=[]
stack.append(11)
stack.append(2)
stack.append(32)
stack.append(3)
stack.append(41)
stack.append(5055)
stack.append(65)

print(stack)
solve(stack)
print(stack)

