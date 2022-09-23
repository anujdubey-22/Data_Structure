'''
Expected Time Complexity: O(M+|search|).
Expected Auxiliary Space: O(M).
M = sum of the length of all strings which is present in the key[] 
'''

#Function to insert string into TRIE.
def insert(root,key):
    #code here
    curr=root
    for i in range(len(key)):
        index= charToIndex(key[i])
        if curr.children[index]==None:
            curr.children[index]=TrieNode()
            
        curr=curr.children[index]
        
    curr.isEndOfWord=True
    return

#Function to use TRIE data structure and search the given string.
def search(root, key):
    #code here
    curr=root
    for i in range(len(key)):
        index=charToIndex(key[i])
        
        if curr.children[index]==None:
            return False
        curr=curr.children[index]
        
    return curr.isEndOfWord

#{ 
#  Driver Code Starts

class TrieNode: 
      
    def __init__(self): 
        self.children = [None]*26
  
        # isEndOfWord is True if node represent the end of the word 
        self.isEndOfWord = False
  
class Trie: 
      
    # Trie data structure class 
    def __init__(self): 
        self.root =TrieNode()
        
#use only 'a' through 'z' and lower case
def charToIndex(ch):
    return ord(ch)-ord('a')

if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=input().strip().split()
        strs=input()
        
        t=Trie()
        
        for s in arr:
            insert(t.root,s)
        
        if search(t.root,strs):
            print(1)
        else:
            print(0)
# } Driver Code Ends