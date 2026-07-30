class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        prefix_sum=0
        count=0
        prefix_count={0:1}
        for i in range(len(nums)):
            prefix_sum+=nums[i]
            if prefix_sum-goal in prefix_count:
                count+=prefix_count[prefix_sum-goal]
            if prefix_sum in prefix_count:
                prefix_count[prefix_sum]+=1
            else:
                prefix_count[prefix_sum]=1
        return count
        