# Last updated: 6/8/2025, 11:54:33 AM
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        m = len(matrix[0])
        n = len(matrix)
        col = m - 1
        while row < n and col >=0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False