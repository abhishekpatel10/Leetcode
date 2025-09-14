# Last updated: 9/14/2025, 1:22:21 PM
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        par = list(range(n))
        size = [0] * n
        def parent(x):
            if x == par[x]:
                return x
            par[x] = parent(par[x])
            return par[x]
        def Union(x,y):
            x1 = parent(x)
            x2 = parent(y)
            if x1 ==x2:
                return
            if size[x1] > size[x2]:
                par[x2] = x1
                size[x1] += size[x2]
            else:
                par[x1] = x2
                size[x2] += size[x1]
        for u,v in connections:
            Union(u,v)
        ans = 0
        for i in range(n):
            if parent(i) == i:
                ans += 1
        return ans - 1
