# Last updated: 6/8/2025, 11:54:49 AM
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        for u,v in prerequisites:
            g[u].append(v)
        
        unvis = 0
        visiting = 1
        visited = 2
        states = [0] * numCourses 
        def dfs(node):
            state = states[node]
            if state == visited:
                return True
            if state == visiting:
                return False
            states[node] = visiting
            for neig in g[node]:
                if not dfs(neig):
                    return False
            states[node] = visited
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True