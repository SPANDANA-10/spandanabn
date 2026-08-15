class Solution(object):
    def reverseStr(self, s, k):
        s=list(s)
        for i in range(0,len(s),2*k):
            s[i:min(i+k,len(s))]=s[i:min(i+k,len(s))][::-1]   
        return "".join(s)
        