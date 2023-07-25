class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # Using a two pointer approach
        # If sum is below, we move down right
        # If sum is above, we move up left
        left, right = 0, len(numbers) - 1

        while (left < right):
            cur = numbers[left] + numbers[right]
            if (cur < target):
                left += 1
            elif (cur > target):
                right -= 1
            else:
                return [left + 1, right + 1]