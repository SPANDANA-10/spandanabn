class Solution(object):
    def minSubArrayLen(self, target, nums):
        left=0
        total=0
        smallest=float('inf')
        for right in range(len(nums)):
            total=total+nums[right]
            while total>=target:
                smallest=min(smallest,right-left+1)
                total-=nums[left]
                left+=1
        if smallest!=float('inf'):
            return smallest
        else:
            return 0

        