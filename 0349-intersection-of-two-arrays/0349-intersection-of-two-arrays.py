class Solution(object):
    def intersection(self, nums1, nums2):
        seen=set()
        for i in nums1:
            if i in nums2:
                seen.add(i)
        return list(seen)
