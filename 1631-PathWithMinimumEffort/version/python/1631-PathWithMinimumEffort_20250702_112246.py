# Last updated: 7/2/2025, 11:22:46 AM
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0
        heap = [(0,0,0)]
        while heap:
            curr_min , r ,c = heapq.heappop(heap)
            if r == n- 1 and c == m -1:
                return curr_min
            dirs = [(0,1),(-1,0),(0,-1),(1,0)]
            for dr , dc in dirs:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    curr_eff = abs(heights[r][c] - heights[nr][nc])
                    max_effort = max(curr_eff , curr_min)
                    if max_effort < dist[nr][nc]:
                        dist[nr][nc] = max_effort
                        heapq.heappush(heap,(max_effort,nr,nc))
        return -1