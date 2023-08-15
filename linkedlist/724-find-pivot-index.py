class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        S = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            rightSum = S - leftSum - nums[i]
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1