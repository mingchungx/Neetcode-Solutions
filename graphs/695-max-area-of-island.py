class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        visited = set()
        # Let i be row
        # Let j be col
        def dfs(i, j):
            # Base case: Out of bounds, or hit a wall
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0 or (i, j) in visited:
                return 0

            # Mark as visited
            visited.add((i, j))

            area = 1
            # Move right
            area += dfs(i, j + 1)
            # Move down
            area += dfs(i + 1, j)
            # Move left
            area += dfs(i, j - 1)
            # Move up
            area += dfs(i - 1, j)

            return area

        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))

        return maxArea