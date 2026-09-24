# Last updated: 9/24/2026, 3:42:40 PM
1class Solution:
2    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
3        
4        n = len(image)
5        m = len(image[0])
6        temp = image[sr][sc]
7        if temp == color:
8            return image
9        self.dfs(sr,sc,image,color,temp,n,m)
10        return image
11    def dfs(self,i,j,image,color,temp,n,m):
12
13        image[i][j] = color
14        
15        dirs = [(0,1),(-1,0),(1,0),(0,-1)]
16        for dr , dc in dirs:
17            nr = dr + i
18            nc = dc + j
19            if 0 <= nr < n and 0 <= nc < m and image[nr][nc] == temp:
20                self.dfs(nr,nc,image,color,temp,n,m)
21        
22        