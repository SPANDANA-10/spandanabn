class Solution(object):
    def maxVowels(self, s, k):
        vowel="aeiou"
        count=0
        max_count=0
        for i in range(len(s)):
            if s[i] in vowel:
                count+=1
            if i>=k:
                if s[i-k] in vowel:
                    count-=1
            max_count=max(max_count,count)
        return max_count
                
            
        