class Solution(object):
    def maximumWealth(self, accounts):
        max=0
        for i in accounts:
            wealth = sum(i)
            if wealth > max:
                max = wealth
        return max