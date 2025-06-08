# Last updated: 6/8/2025, 11:54:46 AM
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for u ,v in prerequisites:
            g[u].append(v)
        unvis = 0
        visiting = 1
        visited = 2
        ans = []
        states = [0] * numCourses
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
            ans.append(node)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return ans
