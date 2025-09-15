# Last updated: 9/15/2025, 7:40:12 PM
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
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 0:
                    continue
                if grid[row][col] == 1:
                    dirs = [(0,1),(1,0),(-1,0),(0,-1)]
                    for dr , dc in dirs:
                        nr = row + dr
                        nc = col + dc
                        if self.isValid(nr,nc,n) and grid[nr][nc] == 1:
                            curr_node = row* n + col
                            adj_node = nr*n+ nc
                            ds.union(curr_node,adj_node)
        max_island = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    continue
                comp = set()
                dirs = [(0,1),(1,0),(-1,0),(0,-1)]
                for dr , dc in dirs:
                    nr = i + dr
                    nc = j + dc
                    if self.isValid(nr,nc,n) and grid[nr][nc] == 1:
                        comp.add(ds.find(nr * n + nc))
                size = 1
                for c in comp:
                    size += ds.size[c]
                max_island = max(max_island, size)
        for cell in range(n*n):
            max_island = max(max_island,ds.size[ds.find(cell)])
        return max_island


