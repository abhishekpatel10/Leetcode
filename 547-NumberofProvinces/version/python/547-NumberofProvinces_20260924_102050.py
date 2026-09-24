# Last updated: 9/24/2026, 10:20:50 AM
1class Solution:
2    def findCircleNum(self, isConnected: List[List[int]]) -> int:
3        n = len(isConnected)
4        vis = [0] * n 
5        ans = 0
6
7        for node in range(n):
8            if vis[node] ==0 :
9                self.dfs(node,isConnected,vis)
10                ans += 1
11                
12        return ans
13    def dfs(self,node,isConnected,vis):
14        vis[node] = 1
15        n = len(isConnected)
16        for nei in range(n):
17            if isConnected[node][nei] == 1 and vis[nei] == 0:
18                self.dfs(nei,isConnected,vis)
19        