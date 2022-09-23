'''
Minimum sum of two numbers formed from digits of an array.
'''

'''
Expected Time Complexity: O(N*logN)
Expected Auxiliary Space: O(1)

'''

class Solution:
    def solve(self, arr, n):
        # code here
        if n==1:
            return arr[0] # for 1 input there is not enough number to add therefor return the single digit array
        even=''
        odd=''
        output=0
        arr.sort()
        
        for i in range(n):
            if i%2==0:
                even+=str(arr[i])
            else:
                odd+=str(arr[i])
                
        output=int(even)+int(odd)
        
        return (output)
        