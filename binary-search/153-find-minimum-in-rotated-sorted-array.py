class Solution:
    def findMin(self, nums: list[int]) -> int:
        # The minimum is the one with a left neighbour that is greater than itself
        # If the position is [0], then the left neighbour is at position [-1]

        left, right = 0, len(nums) - 1
        curMin = nums[0]
        while (left <= right):
            if nums[left] < nums[right]:
                curMin = min(curMin, nums[left])
                break

            mid = (left + right) // 2
            # Now we have the middle value, we need to decide whether to search the left or right
            # Since the array is rotated, then the middle is EITHER a part of the greater rotated part
            # Or the smaller unrotated part
            # We can check this by comparing left
            curMin = min(curMin, nums[mid])
            if nums[mid] >= nums[left]:
                # Then we are in the greater part, so we search right
                left = mid + 1
            else:
                right = mid - 1
        
        return curMin