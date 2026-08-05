class Solution(object):
    def sortedSquares(self, nums):
        left=0
        ans=[0]*len(nums)
        k=len(ans)-1
        right=len(nums)-1
        while left<=right:
            if abs(nums[left])>=abs(nums[right]):
                ans[k]=nums[left]**2
                left+=1
                k-=1
            else:
                ans[k]=nums[right]**2
                right-=1
                k-=1
            
        return ans