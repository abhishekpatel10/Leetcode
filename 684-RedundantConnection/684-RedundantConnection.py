# Last updated: 6/8/2025, 11:53:58 AM
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n+1)]
        rank = [1] * (n+1)

        def find(n):
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]
        def union(p1,p2):
            p1 = find(p1) 
            p2 = find(p2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p2] += rank[p1]
            else:
                par[p1] = p2
                rank[p1] += rank[p2]
            return True
        for u ,v in edges:
            if not union(u,v):
                return [u,v]
