class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        best_sum=nums[0]+nums[1]+nums[2]
        sum=0
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            while left<right:
                sum=nums[i]+nums[left]+nums[right]
                if abs(sum-target)<abs(best_sum-target):
                    best_sum=sum
                if sum==target:
                    return sum
                elif sum<target:
                    left+=1
                else:
                    right-=1
        return best_sum