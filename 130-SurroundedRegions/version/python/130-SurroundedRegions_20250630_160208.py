# Last updated: 6/30/2025, 4:02:08 PM
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        def dfs(i,j):
            board[i][j] = 'T'
            dirs = [(0,1),(1,0),(-1,0),(0,-1)]
            for dr , dc in dirs:
                nr = dr + i
                nc = dc + j
                if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == 'O':
                    dfs(nr,nc)

        for i in range(n):
            for j in range(m):
                if (i == 0 or i == n - 1 or j == 0 or j == m -1) and board[i][j] == 'O':
                    dfs(i,j)
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        