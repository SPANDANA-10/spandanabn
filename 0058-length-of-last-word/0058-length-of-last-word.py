class Solution(object):
    def lengthOfLastWord(self, s):
        res=""
        for i in range(len(s)-1,-1,-1):
            if s[i].isalpha():
                res+=s[i]
            elif len(res)==0:
                continue
            else:
                break
        return len(res)
            
        