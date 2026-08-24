class Solution(object):
    def frequencySort(self, s):
        count={}
        for ch in s:
            if ch in count:
                count[ch]+=1
            else:
                count[ch]=1
        pairs=[]
        for ch in count:
            pairs.append((ch,count[ch]))
        pairs.sort(key=lambda x:x[1],reverse=True)
        res=""
        for ch,freq in pairs:
            res+=(ch*freq)
        return res

        