# Last updated: 4/3/2025, 5:43:02 PM
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
        maxRow = 0
        maxCol = 0
        for stone in stones:
            maxRow = max(maxRow, stone[0])
            maxCol = max(maxCol, stone[1])
            
        ds = UnionFind(maxRow + maxCol + 2)# We have MAX_ROW rows and MAX_ROW columns

        stoneNodes = {}  # to keep track of unique rows and columns
        for stone in stones:
            nodeRow = stone[0]
            nodeCol = stone[1] + maxRow + 1  # Adjust column index to differentiate from rows
            ds.union(nodeRow, nodeCol)
            stoneNodes[nodeRow] = 1
            stoneNodes[nodeCol] = 1
        cnt = 0
        for node in stoneNodes:
            if ds.find(node) == node:
                cnt += 1

        # Step 5: Return the result: total stones - number of distinct connected components
        return len(stones) - cnt