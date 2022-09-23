'''
Expected Time Complexity: O(log(max(N,M)))
Expected Auxiliary Space: O(1)

Using Greatest Common Divisor(GCD) .
'''

class Solution:
    def rooms(self, N, M):
        # code here
        def gcd(a,b):
            if b==0:
                return a
            return gcd(b,a%b)
            
        if N>M:
            ans=gcd(N,M)
        else:
            ans=gcd(M,N)
            
        return N//ans+M//ans
