class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # We need to keep track of prefix and postfix
        n = len(nums)
        output = [1] * n
        
        # Get the prefix values from accumulating
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]
        
        # Get the postfix values from accumulating
        postfix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        
        return output