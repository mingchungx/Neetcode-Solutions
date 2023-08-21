class Solution:
    def rob(self, nums: list[int]) -> int:
        #@cache
        def dp(i):
            if (i < 0):
                return 0
            return max(dp(i - 2) + nums[i], dp(i - 1))
        return dp(len(nums) - 1)