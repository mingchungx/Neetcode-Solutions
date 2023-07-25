class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # We keep a hash map of numbers in nums
        ht = {}
        for i in range(len(nums)):
            # We will try to find a complement which adds to target
            complement = target - nums[i]

            # If it exists, we return (although it always does according to statement)
            if complement in ht:
                return [ht[complement], i]
            ht[nums[i]] = i
        return None