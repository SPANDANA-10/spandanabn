class Solution(object):
    def isAnagram(self, s, t):
        count={}
        for ch in s:
            if ch in count:
                count[ch]+=1
            else:
                count[ch]=1
        sum={}
        for ch in t:
            if ch in sum:
                sum[ch]+=1
            else:
                sum[ch]=1
        if count==sum:
            return True
        else:
            return False
        

        