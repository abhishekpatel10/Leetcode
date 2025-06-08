# Last updated: 6/8/2025, 11:52:42 AM
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        col = len(heights[0])
        heap = [(0,0,0)]
        effort = [[float('inf')] * col for _ in range(row)]
        effort[0][0] = 0
        while heap:
            min_eff,r,c = heapq.heappop(heap)
            if r == row-1 and c == col - 1:
                return min_eff
            dirs = [(0,1),(1,0),(-1,0),(0,-1)]
            for dr,dc in dirs:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < row and 0 <= nc < col :
                    curr_min = abs(heights[r][c] - heights[nr][nc])
                    max_effort = max(min_eff,curr_min)
                    if max_effort < effort[nr][nc]:
                        effort[nr][nc] = max_effort
                        heapq.heappush(heap,(max_effort,nr,nc))
        return -1


