'''
Expected Time Complexity: O(N)
Expected Space Complexity: O(N)
'''

'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    #Your Function Should return True/False
    def isHeap(self, root):
        #Code Here
        q=[]
        q.append(root)
        bool=False # for assuring the completeness of max heap
        
        while len(q)>0:
            curr=q.pop(0)
            if curr.left!=None:
                if bool or curr.left.data>curr.data:
                    return False
                else:
                    q.append(curr.left)
            else:
                bool=True # if anytime the left node is not present ,that means after this level no other node should be present 
                
            if curr.right!=None:
                if bool or curr.right.data>curr.data:
                    return False
                else:
                    q.append(curr.right)
            else:
                bool=True # if anytime the right node is not present ,that means after this level no other node should be  present 
                
        return True

