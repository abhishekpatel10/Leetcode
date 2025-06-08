# Last updated: 6/8/2025, 11:54:07 AM
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        vis = [False] * n
        ans = 0
        def dfs(city):
            for nei in range(n):
                if isConnected[city][nei] == 1 and not vis[nei]:
                    vis[nei] = True
                    dfs(nei)

        for city in range(n):
            if not vis[city]:
                vis[city] = True
                dfs(city)
                ans += 1
        return ans