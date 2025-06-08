# Last updated: 6/8/2025, 11:55:07 AM
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        def bfs():
            q = deque()
            for i in range(m):
                for j in range(n):
                    if (i == 0 or i == m - 1 or j ==0 or j == n - 1) and board[i][j] =='O':
                        q.append((i,j))
            while q:
                i , j = q.popleft()
                dir = [(1,0), (0,1),(-1,0), (0,-1)]
                if board[i][j] == 'O':
                    board[i][j] = 'T'
                    for di , dj in dir:
                        r = i +di
                        c= j + dj
                        if 0<=r<m and 0 <=c < n :
                            q.append((r,c))
        bfs()
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'T':
                    board[i][j] = 'O'