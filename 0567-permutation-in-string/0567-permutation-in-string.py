class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1)>len(s2):
            return False
        s1_count={}
        s2_count={}
        for char in range(len(s1)):

            s1_count[s1[char]] = s1_count.get(s1[char], 0) + 1
            s2_count[s2[char]] = s2_count.get(s2[char], 0) + 1
        if s1_count==s2_count:
            return True
        left=0
        for right in range(len(s1),len(s2)):
            s2_count[s2[right]] = s2_count.get(s2[right], 0) + 1
            s2_count[s2[left]]-=1
           
            if s2_count[s2[left]]==0:
                del s2_count[s2[left]]
            left+=1
        
            if s1_count==s2_count:
                return True
        return False


        