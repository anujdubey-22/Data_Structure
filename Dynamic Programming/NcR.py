

mod=1000000000+7
class Solution:
    def nCr(self, n, r):
        #
        if r>n:
            return 0
        fact=1
        for i in range(n,n-r,-1):
            fact*=i
            
        fact2=1
        for i in range(1,r+1):
            fact2*=i
    
        return (fact//fact2)%mod