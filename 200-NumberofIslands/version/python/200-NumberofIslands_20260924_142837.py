# Last updated: 9/24/2026, 2:28:37 PM
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        n = len(grid)
4        m = len(grid[0])
5        vis = [[0] * m for _ in range(n)]
6        
7        ans = 0
8        for i in range(n):
9            for j in range(m):
10                if vis[i][j] == 0 and grid[i][j] == "1":
11                    ans += 1
12                    self.bfs(i,j,grid,vis,n,m)
13        return ans
14    def bfs(self,i,j,grid,vis,n,m):
15        vis[i][j] = 1
16        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
17        q = deque([(i, j)])
18        while q:
19            row,col = q.popleft()
20            for dr, dc in directions:
21                nr = row + dr
22                nc = col + dc
23                if ( 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == "1" and vis[nr][nc] == 0):
24                    vis[nr][nc] = 1
25                    q.append((nr,nc))
26        
27