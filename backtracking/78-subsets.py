class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        output = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                output.append(subset.copy())
                return
            
            # include i
            subset.append(nums[i])
            dfs(i + 1)

            # don't include i
            subset.pop()
            dfs(i + 1)

        dfs(0)

        return output