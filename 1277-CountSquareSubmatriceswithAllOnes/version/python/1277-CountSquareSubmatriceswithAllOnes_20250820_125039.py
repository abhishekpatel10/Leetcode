# Last updated: 8/20/2025, 12:50:39 PM
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        total = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1 and i > 0 and j > 0:
                    matrix[i][j] = min(
                        matrix[i-1][j],
                        matrix[i][j-1],
                        matrix[i-1][j-1]
                    ) + 1
                total += matrix[i][j]

        return total
        