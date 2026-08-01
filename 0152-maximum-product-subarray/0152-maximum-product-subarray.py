class Solution(object):
    def maxProduct(self, nums):
        max_product=nums[0]
        min_product=nums[0]
        answer=nums[0]
        for i in range(1,len(nums)):
            prev_max=max_product
            prev_min=min_product
            new_max=max(nums[i],nums[i]*prev_max,nums[i]*prev_min)
            new_min=min(nums[i],nums[i]*prev_max,nums[i]*prev_min)
            max_product=new_max
            min_product=new_min
            answer=max(answer,max_product)
        return answer


