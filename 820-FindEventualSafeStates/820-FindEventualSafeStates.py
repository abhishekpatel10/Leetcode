# Last updated: 6/8/2025, 11:53:18 AM
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        n = len(graph)
        for i in range(n):
            for v in graph[i]:
                g[i].append(v)
        unvis = 0
        visiting = 1
        visited = 2
        ans = []
        states = [0] * n
        def dfs(node):
            state = states[node]
            if state == visiting:
                return False
            elif state == visited:
                return True
            states[node] = visiting
            for nei in g[node]:
                if not dfs(nei):
                    return False
            states[node] = visited
            return True
        for i in range(n):
            if dfs(i):
                ans.append(i)
        return ans
        