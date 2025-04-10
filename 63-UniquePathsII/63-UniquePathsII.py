# Last updated: 4/10/2025, 4:11:33 PM
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        prev = [0] *m
        if obstacleGrid[0][0] == 1:
            return 0
        for i in range(n):
            temp = [0] * m
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    temp[j] = 0
                elif i == 0 and j == 0:
                    temp[j] = 1
                else:
                    up = 0
                    if i > 0:
                        up += prev[j]
                    left = 0
                    if j > 0:
                        left += temp[j-1]
                    temp[j] = up + left
            prev = temp
        return prev[m-1]

            
        