# Last updated: 9/24/2026, 3:32:22 PM
1class Solution:
2    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
3        
4        n = len(image)
5        m = len(image[0])
6        temp = image[sr][sc]
7        if temp == color:
8            return image
9        image[sr][sc] = color
10        q = deque()
11        q.append((sr,sc))
12        while q:
13            for _ in range(len(q)):
14                row,col = q.popleft()
15                dirs = [(0,1),(-1,0),(1,0),(0,-1)]
16                for dr , dc in dirs:
17                    nr = dr + row
18                    nc = dc + col
19                    if 0 <= nr < n and 0 <= nc < m and image[nr][nc] == temp:
20                        image[nr][nc] = color
21                        q.append((nr,nc))
22        
23        return image