class Solution(object):
    def repeatedSubstringPattern(self, s):
        for leng in range(1,len(s)):
            if len(s)%leng==0:
                pattern=s[:leng]
                if pattern*(len(s)//leng)==s:
                    return True
        return False
                

        