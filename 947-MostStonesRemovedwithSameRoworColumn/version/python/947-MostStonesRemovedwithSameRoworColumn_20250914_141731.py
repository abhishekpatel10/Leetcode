# Last updated: 9/14/2025, 2:17:31 PM
class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))  # Initially, each element is its own parent
        self.rank = [0] * size  # Rank will help to optimize union operation

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
                                    
    def union(self, x: int, y: int) -> None:
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            # Union by rank
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        maxRows = 0
        maxCols = 0
        for stone in stones:
            maxRows = max(maxRows,stone[0])
            maxCols = max(maxCols,stone[1])
        ds = UnionFind(maxRows+maxCols + 2)
        stoneNode = {}
        for stone in stones:
            nodeRow = stone[0]
            nodeCol = stone[1] + maxRows + 1
            ds.union(nodeRow,nodeCol)
            stoneNode[nodeRow] = 1
            stoneNode[nodeCol] = 1
        ans = 0
        for node in stoneNode:
            if ds.find(node) == node:
                ans += 1
        return len(stones) - ans