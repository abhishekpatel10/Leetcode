# Last updated: 6/8/2025, 11:53:59 AM
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows = len(grid)
        cols = len(grid[0])
        def dfs(i,j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return 1+dfs(i+1,j) +dfs(i-1,j) + dfs(i,j+1) + dfs(i,j-1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    currentArea = dfs(i,j)
                    if currentArea > max_area:
                        max_area = currentArea
        return max_area