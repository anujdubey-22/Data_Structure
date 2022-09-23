'''
Expected Time Complexity:O(n)
Expected Auxiliary Space: O(n) 
'''

class Solution:
    def findMaxLen(ob, S):
        # code here 
        stack=[]
        stack.append(-1)
        maxx=0
        
        for i in range(0,len(S)):
            if S[i]=='(':
                stack.append(i)
                
            else:
                stack.pop()
                if len(stack)==0:
                    stack.append(i)
                else:
                    length=i-stack[-1]
                    maxx=max(maxx,length)
                    
        return maxx
                    