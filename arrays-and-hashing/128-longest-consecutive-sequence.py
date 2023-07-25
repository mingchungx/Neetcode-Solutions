class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # The start of a sequence is always the leftmost neighbour on the numberline
        nums = set(nums)
        maxLength, length = 0, 0
        for i in nums:
            if i - 1 not in nums:
                # Then we have the start of a sequence
                j = i
                while (j in nums):
                    length += 1
                    maxLength = max(maxLength, length)
                    j += 1
            length = 0
        return maxLength