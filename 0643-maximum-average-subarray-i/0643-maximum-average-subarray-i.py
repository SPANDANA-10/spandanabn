class Solution(object):
    def findMaxAverage(self, nums, k):
        
        win_sum=sum(nums[:k])
        win_avg=win_sum/float(k)
        max_avg=win_avg
        for i in range(len(nums)-k):
            win_sum=(win_sum-nums[i]+nums[i+k])
            win_avg=win_sum/float(k)
            max_avg=max(max_avg,win_avg)
        return max_avg


        