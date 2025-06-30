# Last updated: 6/30/2025, 3:14:28 PM
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        q = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    q.append((i,j))
                if mat[i][j] == 1:
                    mat[i][j] = float('inf')
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                dirs = [(0,1),(1,0),(-1,0),(0,-1)]
                for dr , dc in dirs:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < n and 0 <= nc < m and mat[nr][nc] > mat[r][c] + 1:
                        mat[nr][nc] = mat[r][c] + 1
                        q.append((nr,nc))
        return mat