# Last updated: 7/1/2025, 11:35:08 AM
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        n = len(graph)
        indegree = [0] * n
        for i in range(n):
            for u in graph[i]:
                g[u].append(i)
                indegree[i] += 1
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
                
        ans = []
        while q:
            curr = q.popleft()
            ans.append(curr)
            for nei in g[curr]:
                indegree[nei] -=1
                if indegree[nei] == 0:
                    q.append(nei)
        return sorted(ans)