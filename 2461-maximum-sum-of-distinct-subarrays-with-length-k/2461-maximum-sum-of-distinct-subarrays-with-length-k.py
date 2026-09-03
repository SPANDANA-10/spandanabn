class Solution(object):
    def maximumSubarraySum(self, nums, k):
        win_sum=sum(nums[:k])
        max_sum=0
        count={}
        for i in range(k):
            count[nums[i]]=count.get(nums[i],0)+1
        if len(count)==k:
            max_sum=win_sum
        for i in range(len(nums)-k):
            count[nums[i]]-=1
            if count[nums[i]]==0:
                del count[nums[i]]
            count[nums[i+k]]=count.get(nums[i+k],0)+1
            win_sum=win_sum-nums[i]+nums[i+k]
            if len(count)==k:
                max_sum=max(max_sum,win_sum)
        return max_sum
        

        