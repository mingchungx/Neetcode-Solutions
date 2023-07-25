class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        output = []
        n = len(nums)
        for i in range(n):
            # If we're at a duplicate
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Using two sum sorted approach with two pointers
            left, right = i + 1, n - 1
            while (left < right):
                a, b, c = nums[i], nums[left], nums[right]
                tripletSum = a + b + c

                if tripletSum < 0:
                    left += 1
                elif tripletSum > 0:
                    right -= 1
                else:
                    output.append([a, b, c])
                    # Now we want to find the other possibilities with a as the fixed number
                    left += 1
                    while (nums[left] == nums[left - 1] and left < right):
                        left += 1
        return output
