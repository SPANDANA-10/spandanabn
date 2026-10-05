class Solution(object):
    def minWindow(self, s, t):
        left=0
        count={}
        target={}
        have=0
        res=[-1,-1]
        res_len=float("inf")
        for char in t:
            target[char]=target.get(char,0) + 1
        need=len(target)
        for right in range(len(s)):
            count[s[right]]=count.get(s[right],0) + 1
            if s[right] in target and count[s[right]] == target[s[right]]:
                have+=1
            while have==need:
                if right-left+1<res_len:
                    res=[left,right]
                    res_len=right-left+1
                count[s[left]]-=1
                if s[left] in target and count[s[left]]<target[s[left]]:
                    have-=1
                left+=1
        l, r = res
        return s[l : r + 1] if res_len != float("inf") else ""
            
