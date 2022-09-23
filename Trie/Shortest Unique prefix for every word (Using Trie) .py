'''
Use FREQUENCY APPRAOCH . 
Expected Time Complexity: O(N*length of each word)
Expected Auxiliary Space: O(N*length of each word)
'''

import sys
sys.setrecursionlimit(10**7)
class TrieNode :
    def __init__(self):
        self.childs=[None]*26
        self.IsBool=False
        self.freq=0
        
class Trie:
    def __init__(self):
        self.root=TrieNode()
    
    def insert(self,word):
        curr=self.root
        for i in range(len(word)):
            if curr.childs[ord(word[i])-ord('a')]==None:
                curr.childs[ord(word[i])-ord('a')]=TrieNode()
            curr=curr.childs[ord(word[i])-ord('a')]
            curr.freq+=1
        curr.IsBool=True
        return
        
    def findPrefix(self,word):
        output=''
        curr=self.root
        for i in range(len(word)):
            if curr.childs[ord(word[i])-ord('a')]!=None:
                curr=curr.childs[ord(word[i])-ord('a')]
                if curr.freq>1:
                    output+=word[i]
                elif curr.freq==1:
                    output+=word[i]
                    return output
        #return output
    
class Solution:
    def findPrefixes(self, arr, N):
        # code here 
        t=Trie()
        for i in range(N):
            t.insert(arr[i])
        
        ans=[]
        
        for j in range(N):
            word=t.findPrefix(arr[j])
            ans.append(word)
        
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(str,input().split()))
        
        ob = Solution()
        res = ob.findPrefixes(arr,N)
        for i in res:
            print(i,end=" ")
        print()

