# Last updated: 9/12/2025, 2:02:19 PM
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u , v , cost in  roads:
            graph[u].append((v, cost))
            graph[v].append((u, cost))
        ways = [0] * n
        ways[0] = 1
        dist = [float('inf')] * n
        dist[0] = 0
        heap = [(0,0)]
        MOD = 10**9 + 7
        while heap:
            curr_dist, curr_node = heapq.heappop(heap)

            # Skip if we already found a better distance
            if curr_dist > dist[curr_node]:
                continue

            for nei, cost in graph[curr_node]:
                new_dist = curr_dist + cost

                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    ways[nei] = ways[curr_node]
                    heapq.heappush(heap, (new_dist, nei))

                elif new_dist == dist[nei]:
                    ways[nei] = (ways[nei] + ways[curr_node]) % MOD 

        return ways[n - 1] 