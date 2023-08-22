class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        endpoint = (m - 1, n - 1)

        obstacles = set()

        #@cache
        def dfs(i, j):
            if (i >= m) or (j >= n) or (i < 0) or (j < 0):
                return 0
            if obstacleGrid[i][j] == 1:
                # Mark as an obstacle
                obstacles.add((i, j))
            if (i, j) in obstacles:
                return 0
            if (i, j) == endpoint:
                return 1

            paths = 0

            # Move right
            paths += dfs(i, j + 1)

            # Move down
            paths += dfs(i + 1, j)

            return paths

        return dfs(0, 0)