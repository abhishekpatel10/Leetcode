# Last updated: 7/23/2025, 4:12:42 PM
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stc = []
        ans = float('-inf')
        n = len(heights)
        for i in range(n):
            while stc and heights[i] < heights[stc[-1]]:
                temp = heights[stc.pop()]
                width = i if not stc else i - stc[-1] - 1
                ans = max(ans,temp*width)
            stc.append(i)
        while stc:
            h = heights[stc.pop()]
            width = n if not stc else n - stc[-1] -1 
            ans = max(ans , width* h)
        return ans
