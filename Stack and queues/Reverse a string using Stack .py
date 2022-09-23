'''
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
'''

def reverse(S):
    
    #Add code here
    stack=[]
    for i in range(len(S)):
        stack.append(S[i])
        
    output=""
    for i in range(len(S)):
        output+=(stack.pop())
    return output
    