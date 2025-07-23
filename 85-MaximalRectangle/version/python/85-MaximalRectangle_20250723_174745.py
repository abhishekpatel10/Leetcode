# Last updated: 7/23/2025, 5:47:45 PM
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = float('-inf')
        stc = []
        n = len(heights)
        for i in range(n):
            while stc and heights[stc[-1]] > heights[i]:
                height = heights[stc.pop()]
                width = i if not stc else i - stc[-1] - 1
                area = max(area,height*width)
            stc.append(i)
        while stc:
            height = heights[stc.pop()]
            width = n if not stc else n - stc[-1] - 1
            area = max(area,width*height)
        return area
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix[0])
        n = len(matrix)
        max_area = float('-inf')
        p_sum = [[0 for _ in range(m)] for _ in range(n)]
        for j in range(m):
            summ = 0
            for i in range(n):
                summ += int(matrix[i][j])
                if matrix[i][j] == "0":
                    summ = 0
                p_sum[i][j] = summ
        for i in range(n):
            max_area = max(max_area,self.largestRectangleArea(p_sum[i]))
        return max_area
