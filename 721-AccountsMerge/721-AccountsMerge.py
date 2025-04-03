# Last updated: 4/3/2025, 7:07:22 PM
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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        ds = UnionFind(n+1)
        mapMailNode = {}
        for i in range(n):
            for j in range(1,len(accounts[i])):
                mail = accounts[i][j]
                if mail not in mapMailNode:
                    mapMailNode[mail] = i
                else:
                    ds.union(i,mapMailNode[mail])
        mergedMail = [[] for _ in range(n)]
        
        # Group emails by the root of the account
        for mail, node in mapMailNode.items():
            root = ds.find(node)
            mergedMail[root].append(mail)
            
        ans = []
        for i in range(n):
            if mergedMail[i]:
                # Sort emails lexicographically
                mergedMail[i].sort()
                temp = [accounts[i][0]] + mergedMail[i]  # Add the name to the merged emails
                ans.append(temp)
        return ans