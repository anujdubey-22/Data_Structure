'''
Expected Time Complexity : O(1) for push() and O(N) for pop() or O(N) for push() and O(1) for pop()  
Expected Auxilliary Space : O(1). 
'''
################################# Using 1 Stack #################################################

def Push(x,stack1,stack2):
    '''
    x: value to push
    stack1: list
    stack2: list
    '''
    #code here
    stack1.append(x)
    n=len(stack1)
    for i in range(0,n-1):
        value=stack1.pop(0)
        stack1.append(value)

#Function to pop an element from queue by using 2 stacks.
def Pop(stack1,stack2):
    
    '''
    stack1: list
    stack2: list
    '''
    #code here
    if len(stack1)>0:
        return stack1.pop()
    else:
        return -1



########################### Using 2 Stacks #####################################################


def Push(x,stack1,stack2):
    '''
    x: value to push
    stack1: list
    stack2: list
    '''
    #code here
    stack1.append(x)
    while len(stack2)!=0:
        value=stack2.pop(0)
        stack1.append(value)
    while len(stack1)>0:
        value=stack1.pop(0)
        stack2.append(value)

#Function to pop an element from queue by using 2 stacks.
def Pop(stack1,stack2):
    
    '''
    stack1: list
    stack2: list
    '''
    #code here
    if len(stack2)>0:
        return stack2.pop()
    return -1
