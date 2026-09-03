class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        win_sum=sum(arr[:k])
        win_avg=win_sum/float(k)
        count=0
        if win_avg>=threshold:
                count+=1
        for i in range(len(arr)-k):
            win_sum=win_sum-arr[i]+arr[i+k]
            win_avg=win_sum/float(k)
            if win_avg>=threshold:
                count+=1
            
        return count

        