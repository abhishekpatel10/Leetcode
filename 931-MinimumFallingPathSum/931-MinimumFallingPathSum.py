# Last updated: 4/11/2025, 1:22:51 AM
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        curr_min = float('inf')
        prev = [0] * n
        for i in range(n):
            prev[i] = matrix[0][i]
        for i in range(1,n):
            temp = [0] * n
            for j in range(n):
                up = matrix[i][j] + prev[j]
                
                downleft = matrix[i][j]
                if j - 1 >= 0:
                    downleft += prev[j-1]
                else:
                    downleft += float('inf') 
                downright = matrix[i][j]
                if j+1 <n:
                    
                    downright += prev[j+1]
                else:
                    downright += float('inf')
                temp[j] = min(up,downleft,downright)
            prev = temp
        return min(prev)
                

