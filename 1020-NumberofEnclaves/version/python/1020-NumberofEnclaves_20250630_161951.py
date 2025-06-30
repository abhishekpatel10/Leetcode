# Last updated: 6/30/2025, 4:19:51 PM
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        q = deque()
        for i in range(n):
            for j in range(m):
                if ( i== 0 or i == n - 1 or j == 0 or j == m-1) and grid[i][j] == 1:
                    q.append((i,j))
                    grid[i][j] = 0
                
                    
        
        while q:
            r  ,c = q.popleft()
            dirs = [(0,1),(1,0),(-1,0),(0,-1)]
            for dr,dc in dirs:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < n and 0 <=nc < m and grid[nr][nc] == 1:

                    grid[nr][nc] = 0
                    q.append((nr,nc))
        ans = 0
        print(grid)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ans += 1
        return ans