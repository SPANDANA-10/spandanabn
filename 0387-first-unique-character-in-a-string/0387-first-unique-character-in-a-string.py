class Solution(object):
    def firstUniqChar(self, s):
        for i in range(len(s)):
            if s[i] in s[:i] or s[i] in s[i+1:]:
                continue
            else:
                return i 
        return -1
        