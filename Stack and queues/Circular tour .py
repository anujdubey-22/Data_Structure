'''
Expected Time Complexity: O(N)
Expected Auxiliary Space : O(1)
'''

'''
    lis[][0]:Petrol
    lis[][1]:Distance
'''

class Solution:
    
    #Function to find starting point where the truck can start to get through
    #the complete circle without exhausting its petrol in between.
    def tour(self,lis, n):
        #Code here
        extrafuel=0 # if petrol is saved after reaching the distance.
        required=0 # if petrol ends before reaching the distance then store the required petrol in this variable 
        start=0
        i=0
        while i<(len(lis)):
            extrafuel+=lis[i][0]-lis[i][1]
            if extrafuel<0: # if any time extrafuel<0 then this means this index is not the ans .
                required+=extrafuel
                extrafuel=0 # assigning the extrafuel as 0 so that we can start from new index ownwards.
                start=i+1 #increase the index  as the current index can't be the ans. the ans should be ahead of this current index.
            i+=1
        if extrafuel+required>0:
            return start
        return -1