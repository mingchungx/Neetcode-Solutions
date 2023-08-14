class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        n = len(nums)

        # Making ans of length 2n
        ans = [0] * 2 * n

        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]

        return ans

# Note: an easy solution is simply "return nums + nums"
