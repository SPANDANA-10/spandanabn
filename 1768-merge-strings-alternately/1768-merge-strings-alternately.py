class Solution(object):
    def mergeAlternately(self, word1, word2):
        left=0
        right=0
        s=[]
        while left<len(word1) or right<len(word2):
            if left<len(word1):
                s.append(word1[left])
                left+=1
            if right<len(word2):
                s.append(word2[right])
                right+=1
        return ''.join(s)
            

        