# Last updated: 7/1/2025, 11:10:04 AM
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        node = defaultdict(list)
        for u,v in prerequisites:
            node[v].append(u)
            indegree[u] += 1
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        finish = 0

        while q:
            curr = q.popleft()
            finish +=1
            for nei in node[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return finish == numCourses
