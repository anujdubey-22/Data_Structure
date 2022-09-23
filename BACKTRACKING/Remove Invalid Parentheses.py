class Solution:
    def minRemove(self,s):
        stack=[]
        for i in range(len(s)):
            if s[i]=="(":
                stack.append(s[i])
            elif s[i]==")":
                if len(stack) and stack[-1]=="(":
                    stack.pop()
                else:
                    stack.append(s[i])
        return len(stack)
    
    def solve(self,s,minRemovals):
        global ans, d
        if s in d:   # optimizing before the algo as the same string should not processed again , thus reducing time complexity
            return 
        d[s]=1        # mark the string in dictionary so that again it should not processe in algo 
        if minRemovals==0:
            checkLastTimeStack=self.minRemove(s)
            if checkLastTimeStack==0:
                ans.append(s)
            else:
                return 
        for i in range(len(s)):
            if s[i]==")" or s[i]=="(" :
                left=s[:i]
                right=s[i+1:]
                self.solve(left+right,minRemovals-1)
        
    def removeInvalidParentheses(self, s: str) -> List[str]:
        global ans , d
        ans=[]
        d={} # taking dictionary to optimize the algo
        output=""
        
        minRemovals=self.minRemove(s)
        
        self.solve(s,minRemovals)
        return ans
            