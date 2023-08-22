class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Note the endpoint (complete)
        endpoint = (m - 1, n - 1)

        #@cache
        def dfs(i, j):
            if (i >= m) or (j >= n) or (i < 0) or (j < 0):
                return 0
            if (i, j) == endpoint:
                return 1

            # We can either move right or move down
            paths = 0

            # Move right
            paths += dfs(i, j + 1)

            # Move down
            paths += dfs(i + 1, j)

            return paths

        return dfs(0, 0)
