'''
Expected Time Complexity: O(|S|)
Expected Auixilliary Space: O(|S|)
'''

class Solution:
    
    #Function to evaluate a postfix expression.
    def evaluatePostfix(self, S):
        #code here
        stack=[]
        
        for i in (S):
            if i.isdigit(): # returns True if string is digit . in next step we convert this string digit into integer digit
                stack.append(int(i)) # convert string (number) into integer
                
            else:
                val_2=stack.pop() # pop top 2 elements from stack to perform operations
                val_1=stack.pop()
                if i=='*':
                    stack.append(val_1*val_2)
                elif i=='/':
                    stack.append(val_1//val_2)
                elif i=='+':
                    stack.append(val_1+val_2)
                else:
                    stack.append(val_1-val_2)
        ans=stack.pop()
        return ans
