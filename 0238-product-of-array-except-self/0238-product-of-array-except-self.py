class Solution(object):
    def productExceptSelf(self, nums):
        prefix=[]
        product=1
        for i in range(len(nums)):
            prefix.append(product)
            product*=nums[i]
        product=1
        suffix=[]
        for i in range(len(nums)-1,-1,-1):
            suffix.append(product)
            product*=nums[i]
        suffix.reverse()
        answer=[]
        for i in range(len(nums)):
            answer.append(prefix[i]*suffix[i])
        return answer