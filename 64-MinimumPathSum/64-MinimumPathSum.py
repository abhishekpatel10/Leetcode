# Last updated: 4/10/2025, 5:02:07 PM
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        prev = [0] * m
        for i in range(n):
            temp = [0] * m
            for j in range(m):
                if i == 0 and j == 0:
                    temp[j] = grid[0][0]
                else:
                    up = grid[i][j]
                    if i > 0:
                        up += prev[j]
                    else:
                        up += float('inf')
                    left = grid[i][j]
                    if j >0:
                        left += temp[j-1]
                    else:
                        left += float('inf')
                    temp[j] = min(left,up)
            prev = temp

        return prev[m-1] 
    
        
