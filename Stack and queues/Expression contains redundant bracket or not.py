'''
Expected Time Complxity : O(N)
Expected Auxilliary Space : O(N)
'''

def findRedundant(s):
    stack=[]
    
    for i in range(0,len(s)):
        if s[i]==')':
            if stack[-1]=='(':
                return True
            else:
                while stack[-1]!='(':
                    stack.pop()
                    
                stack.pop()
            
        elif s[i]=='(' or s[i]=='+' or s[i]=='-' or s[i]=='/' or s[i]=='*':
            stack.append(s[i])
    
    return False
    
    

if __name__=='__main__':
    Str = "((a+b))"
    if findRedundant(Str):
        print('yes')
    else:
        print("No")
 
    Str = "(a+(b)/c)"
    if findRedundant(Str):
        print('yes')
    else:
        print("No")
    Str = "(a+b*((c-d)))"
    if findRedundant(Str):
        print('yes')
    else:
        print("No")
    