class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        output = []
        combination = []

        def dfs(i):
            if len(combination) == k:
                # Base case, add
                output.append(combination.copy())
                return
            if i > n:
                # Base case, finished
                return

            # Include i
            combination.append(i)
            dfs(i + 1)

            # Don't include i
            combination.pop()
            dfs(i + 1)

        dfs(1)
        return output