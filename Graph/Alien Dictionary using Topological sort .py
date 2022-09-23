'''
Expected Time Complexity: O(N * |S| + K) , where |S| denotes maximum length.
Expected Space Compelxity: O(K)
'''

from collections import defaultdict

class Solution:
    def findOrder(self,arr, n, k):
    # code here
        d=defaultdict(list)
        indegree=[-1]*26

        for i in range(len(arr)):
            for j in range(len(arr[i])):
                indegree[ord(arr[i][j])-ord('a')]=0    
                
        for i in range(n-1):
            w1=arr[i]
            w2=arr[i+1]
            
            word_len=min(len(w1),len(w2))
            for j in range(0,word_len):
                if w1[j]!=w2[j]:
                    d[w1[j]]+=[w2[j]]
                    indegree[ord(w2[j])-ord('a')]+=1
                    break
        count=0
        q=[]
        ans=''
        for i in range(26):
            if indegree[i]==0:
                q.append(chr(i+97))
                
        while len(q)>0:
            word=q.pop(0)
            ans+=word
            count+=1
            for string in d[word]:
                indegree[ord(string)-ord('a')]-=1
                if indegree[ord(string)-ord('a')]==0:
                    q.append(string)
                    
        return ans
    