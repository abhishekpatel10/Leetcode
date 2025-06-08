# Last updated: 6/8/2025, 11:54:08 AM
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        q = deque()
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    q.append((i,j))
                if mat[i][j] == 1:
                    mat[i][j] = float('inf')
        while q:
            r , c = q.popleft()
            dir = [(0,1),(1,0),(0,-1),(-1,0)]
            for dr , dc in dir:
                nr = r+dr
                nc = c + dc
                if 0 <=nr < row and 0 <=nc< col and mat[nr][nc] > mat[r][c] +1:
                    mat[nr][nc] = mat[r][c] + 1
                    q.append((nr,nc))
        return mat