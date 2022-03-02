'''The task is to calculate the number of distinct strings 
that can be obtained after performing exactly one swap.'''

def countstring(S):
    s=[0]*26
    ans=0;flag=False
    for i in range(len(S)):
        ans+=i-s[ord(S[i])-ord('a')]
        s[ord(S[i]) - ord('a')]+=1
        if s[ord(S[i])-ord('a')]>=2:
            flag=True
    if flag:
        ans+=1
    return ans