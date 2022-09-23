def palindrom(string):
    if len(string)<=1:
        return True
    else:
        i=0
        j=len(string)-1
        
        while i<=j:
            if string[i]!=string[j]:
                return False
            i+=1
            j-=1
        return True

def solve(s,output,ans):
    if len(s)==0:
        ans.append(output)
        return 
    for i in range(len(s)):
        string=s[:i+1]
        if palindrom(string):
            solve(s[i+1:],output+string+" ",ans)
ans=[]
s='nitin'
output=''
solve(s,output,ans)
print(ans)