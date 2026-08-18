class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        count={}
        for ch in ransomNote:
            count[ch]=count.get(ch,0)+1
        sum={}
        for ch in magazine:
            sum[ch]=sum.get(ch,0)+1
        for ch in count:
            if ch not in sum or count[ch]>sum[ch]:
                return False
        return True

        