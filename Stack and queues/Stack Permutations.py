'''
    Stack Permutations (Check if an array is stack permutation of other)
    OR
    Validate Stack Sequences
'''

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        n=len(pushed)
        j=0
        for i in range(0,n):
            stack.append(pushed[i])
            
            while len(stack)>0 and popped[j]==stack[-1]:
                stack.pop()
                j+=1
        if i==n-1 and j==n and len(stack)==0:
            return True
        else:
            return False
            