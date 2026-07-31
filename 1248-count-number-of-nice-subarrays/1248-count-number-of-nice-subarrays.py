class Solution(object):
    def numberOfSubarrays(self, nums, k):
        prefix_sum=0
        count=0
        prefix_count={0:1}
        for i in range(len(nums)):
            if nums[i]%2==0:
                prefix_sum+=0
            else:
                prefix_sum+=1
            if prefix_sum-k in prefix_count:
                count+=prefix_count[prefix_sum-k]
            if prefix_sum in prefix_count:
                prefix_count[prefix_sum]+=1
            else:
                prefix_count[prefix_sum]=1
        return count

            

        