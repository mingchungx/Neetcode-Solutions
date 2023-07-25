class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxA = 0
        left, right = 0, len(height) - 1
        while (left < right):
            x = right - left
            y = min(height[left], height[right])
            maxA = max(maxA, x * y)
            # Now we must make the choice to shift the left or right pointer
            # At most, we will lose y units of area by shifting a pointer
            if height[left] == y and height[right] != y:
                left += 1
            elif height[right] == y and height[left] != y:
                right -= 1
            else:
                # In this case left and right are the same height, so we'll just move left
                left += 1
        return maxA