# Last updated: 6/8/2025, 11:52:54 AM
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1 
        rank = [0] * n
        par = list(range(n))

        def findPar(x):
            if par[x] != x:
                par[x] = findPar(par[x])
            return par[x]
        
        def Union(y,z):
            root_y = findPar(y)
            root_z = findPar(z)
            if root_y == root_z:
                return 
            if rank[root_y] < rank[root_z]:
                par[root_y] = root_z
            elif rank[root_y] > rank[root_z]:
                par[root_z] = root_y
            else:
                par[root_z] = root_y
                rank[root_y] += 1
        for u, v in connections:
            Union(u, v)
        
        
        components = 0
        for i in range(n):
            if findPar(i) == i:
                components += 1
        
        
        return components - 1