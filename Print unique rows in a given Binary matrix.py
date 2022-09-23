'''
Time complexity: O( ROW x COL ). 
Auxiliary Space: O(ROW).
'''

###  BEST APPROACH  

def uniqueRow(row, col, matrix):
    #complete the function
    s=set()
    ans=[]
    for i in range(row):
        deci=0
        for j in range(col):
            deci=deci+matrix[i][j]*pow(2,j) ### create a decimal index so that we can store it in the SET()  
        if deci not in s:                   ### and this decimal variable is different for diffrent ROW and same for same ROW. 
            s.add(deci)
            ans.append(matrix[i])
            
    return ans
    
matrix=[[0, 1, 0, 0, 1],
                       [1, 0, 1, 1, 0],
                       [0, 1, 0, 0, 1],
                       [1, 0, 1, 0, 0]]

print(uniqueRow(4,5,matrix))