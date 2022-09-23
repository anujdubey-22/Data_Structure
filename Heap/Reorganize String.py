
def solve(s):
    d={}
    for i in range(len(s)):
        if s[i] in d:
            d[s[i]]+=1
            
        else:
            d[s[i]]=1
    #print(d,"d")
    a=[]
    for i in (d):
        a.append([d[i],i])
    #print(a,"a")
    a.sort()
    #print(a,"a")
    output=""
    block=a.pop()
    #print(block[0])
    output+=block[1]
    block[0]-=1
    
    while len(a)>0:
        temp=a.pop()
        output+=(temp[1])
        temp[0]-=1
        if block[0]>0:
            a.append(block)
        block=temp
        a.sort()
    
    if block[0]>0:
        return ""
    return output
    

s="aabcasbba"

print(solve(s))