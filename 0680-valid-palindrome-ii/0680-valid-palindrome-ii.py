class Solution(object):
    def validPalindrome(self, s):
        s=list(s)
        left=0
        right=len(s)-1
        def check(left,right):
            while left<right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True
        while left<right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else :
                return check(left+1,right) or check(left,right-1)
        return True

        