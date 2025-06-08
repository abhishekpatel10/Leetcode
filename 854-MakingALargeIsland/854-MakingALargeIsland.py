# Last updated: 6/8/2025, 11:53:17 AM
class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.size[rootX] < self.size[rootY]:
                rootX, rootY = rootY, rootX
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]
class Solution:
    def isValid(self,nr,nc,n):
        return 0 <= nr < n and 0 <= nc < n
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ds = DisjointSet(n*n)

        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 0:
                    continue
                for dr , dc in dirs:
                    nr = row + dr
                    nc = col + dc
                    if self.isValid(nr,nc,n) and grid[nr][nc] == 1:
                        nodeNo = n * row + col
                        adjNo = nr * n + nc
                        ds.union(nodeNo,adjNo)
        max_island = 0
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    continue
                comp = set()
                for dr , dc in dirs:
                    nr = dr + r
                    nc  = dc + c
                    if self.isValid(nr , nc , n) and grid[nr][nc] == 1:
                        comp.add(ds.find(nr * n + nc))
                
                size = 1
                for c in comp:
                    size += ds.size[c]
                max_island = max(max_island, size)
        for cell in range(n*n):
            max_island = max(max_island,ds.size[ds.find(cell)])
        return max_island
