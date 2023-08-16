class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        visited = set() # Coordinates of visited

        def dfs(i, j):
            # Base case: out of bounds or water
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0:
                return 1
            # Base case: already visited
            if (i, j) in visited:
                return 0
            # Mark as visited
            visited.add((i, j))

            # dfs right
            P = dfs(i, j + 1)
            # dfs down
            P += dfs(i + 1, j)
            # dfs left
            P += dfs(i, j - 1)
            # dfs up
            P += dfs(i - 1, j)

            # Return perimeter
            return P
        
        # Finding one such element that is land (we are guarunteed to have one piece of land)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)