# Last updated: 6/8/2025, 11:52:59 AM
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        row = len(grid)
        col = len(grid[0])
        if grid[0][0] == 1 or grid[row - 1][col - 1] == 1:
            return -1
        dist = [[float('inf')] * col for _ in range(row)]
        dist[0][0] = 1
        q = deque()
        q.append((1,[0,0]))
        while q:
            curr_dis , node = q.popleft()
            r ,c  = node
            dirs = [(0,1),(1,0),(-1,0),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1)]
            for dr ,dc in dirs:
                nr = r+dr
                nc = c+dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0 and dist[nr][nc] > curr_dis +1:
                    dist[nr][nc] = curr_dis +1
                    q.append((dist[nr][nc],[nr,nc]))
        
        return dist[row - 1][col - 1] if dist[row - 1][col - 1] != float('inf') else -1
