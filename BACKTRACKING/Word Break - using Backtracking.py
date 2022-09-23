

class Solution:
    def solve(self,s,dict,n,output):
        global ans
        if len(s)==0:
            ans.append(output[:-1])  #  slicing the last space .. as our output contains space after every words found in dictionary therefor there will be one space left after the last word 
            return                   #  and by slicing it our answer is ready to submit
        
        for i in range(len(s)):
            prefix=s[:i+1]
            
            if prefix in dict:
                self.solve(s[i+1:],dict,n,output+prefix+" ")  # adding space in output after every word found in dictionary
        
        
        
    def wordBreak(self, n, dict, s):
        # code here
        global ans 
        ans=[]
        output=""
        
        self.solve(s,dict,n,output)
        return ans