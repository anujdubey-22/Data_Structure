'''
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

'''

class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        # code here 
        i=0
        for j in range(1,n):
            if M[i][j]==1:
                i=j
                ans=j
            else:
                ans=i
                
        for i in range(0,n):
            if i!=ans:
                if M[i][ans]!=1 or M[ans][i]!=0:
                    return -1
        return ans
            
#####################################################################################################################################

'''
Expected Time Complexity: O(N^2)
Expected Auxiliary Space: O(N)
'''

class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        # code here
        inn=[0]*n
        out=[0]*n
        for i in range(0,n):
            
            for j in range(0,n):
                if M[i][j]==1:
                    inn[j]+=1
                    out[i]+=1

                #else:
        
        for i in range(0,n):
            if inn[i]==n-1 and out[i]==0:
                return i
        return -1
        