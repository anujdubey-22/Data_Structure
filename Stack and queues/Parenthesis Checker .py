
'''
Expected Time Complexity: O(|x|)
Expected Auixilliary Space: O(|x|)
'''



class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        # code here
        if len(x)%2!=0:
            return False
        n=len(x)
        stack=[]
        for i in range(n):
            if x[i]=='(' or  x[i]=='[' or x[i]=='{':
                stack.append(x[i])
            else:
                if len(stack)!=0:
                    value=stack.pop()
                    if value=='(' and x[i]==')' or value=='{' and x[i]=='}' or value=='[' and x[i]==']':
                        continue
                    else:
                        return False
                else:
                    return False
                    
        if len(stack)!=0:
            return False
        else:
            return True
