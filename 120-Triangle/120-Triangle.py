# Last updated: 4/11/2025, 12:33:17 AM
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        prev = [0]*n
        for i in range(n):
            prev[i] = triangle[n-1][i]
        for i in range(n-2,-1,-1):
            temp = [0] * n
            for j in range(i,-1,-1):
                down = triangle[i][j] + prev[j]
                diag = triangle[i][j] + prev[j+1]
                temp[j] = min(down,diag)
            prev = temp
            
        return prev[0]
        

       
    
        