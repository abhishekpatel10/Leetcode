# Last updated: 6/8/2025, 11:53:08 AM
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh +=1
                if grid[i][j] == 2:
                    q.append((i,j))
        time = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                i,j = q.popleft()
                dir = [(1,0),(0,1),(-1,0),(0,-1)]
                for dr , dj in dir:
                    r = i + dr
                    c = j + dj
                    if 0 <= r < m and 0<=c<n and grid[r][c] == 1:
                        grid[r][c] = 2
                        q.append((r,c))
                        fresh -= 1
            time +=1
        return time if fresh == 0 else -1
