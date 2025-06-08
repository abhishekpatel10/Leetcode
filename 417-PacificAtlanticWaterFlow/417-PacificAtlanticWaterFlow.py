# Last updated: 6/8/2025, 11:54:17 AM
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        a_set = set()
        a_que = deque()

        p_set = set()
        p_que = deque()           
        for j in range(n):
            p_set.add((0,j))
            p_que.append((0,j))
        for i in range(m):
            p_set.add((i,0))
            p_que.append((i,0))
        for i in range(m):
            a_set.add((i,n-1))
            a_que.append((i,n-1))
        for j in range(n-1):
            a_set.add((m-1,j))
            a_que.append((m-1,j))
        def bfs(que,seen):
            while que:
                i,j = que.popleft()
                dir = [(0,1),(1,0),(-1,0),(0,-1)]
                for di , dj in dir:
                    r = i+di
                    c = j+dj
                    if 0<=r<m and 0<=c<n and heights[r][c] >= heights[i][j] and (r,c) not in seen:
                        seen.add((r,c))
                        que.append((r,c))
        bfs(a_que,a_set)
        bfs(p_que,p_set)
        return list(a_set.intersection(p_set))
