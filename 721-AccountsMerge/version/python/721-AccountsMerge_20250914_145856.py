# Last updated: 9/14/2025, 2:58:56 PM
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
        mail_map = {}
        for i in range(n):
            for j in range(1,len(accounts[i])):
                mail = accounts[i][j]
                if mail not in mail_map:
                    mail_map[mail] = i
                else:
                    ds.union(i,mail_map[mail])
            
        mergedMail = [[] for _ in range(n)]

        for mail,node in mail_map.items():
            parent = ds.find(node)
            mergedMail[parent].append(mail)
        ans = []
        for i in range(n):
            if mergedMail[i]:
                mergedMail[i].sort()
                final = [accounts[i][0]] + mergedMail[i]
                ans.append(final)
        return ans