# Last updated: 7/2/2025, 11:11:06 AM
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        if grid[0][0] == 1 or grid[m-1][n-1] == 1:
            return -1
        q = deque()
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 1
        q.append((dist[0][0],(0,0)))
        while q:
            curr_dist , node = q.popleft()
            r ,c = node
            dirs = [(0,1),(1,0),(-1,0),(0,-1),(-1,1),(1,-1),(-1,-1),(1,1)]
            for dr , dc in dirs:
                nr = dr + r
                nc = dc + c
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 0 and dist[nr][nc] > dist[r][c] + 1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((dist[nr][nc],(nr,nc)))
        return dist[m-1][n-1] if dist[m-1][n-1] != float('inf') else -1