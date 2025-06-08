# Last updated: 6/8/2025, 11:53:05 AM
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        def dfs(r , c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return
            dir = [(1,0),(0,1),(-1,0),(0,-1)]
            grid[r][c] = 0 
            for dr , dc in dir:
                dfs(r+dr,c+dc)

           

        for i in range(rows):  
            if grid[i][0] == 1:  # Left boundary
                dfs(i, 0)
            if grid[i][cols - 1] == 1:  # Right boundary
                dfs(i, cols - 1)

        for j in range(cols):  
            if grid[0][j] == 1:  # Top boundary
                dfs(0, j)
            if grid[rows - 1][j] == 1:  # Bottom boundary
                dfs(rows - 1, j)
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    count +=1
        return count