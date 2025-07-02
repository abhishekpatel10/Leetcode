# Last updated: 7/2/2025, 11:38:17 AM
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u , v , cost in times:
            graph[u].append((v,cost))
        dist = [float('inf')] * (n+1)
        dist[k] = 0
        q = [(k,0)]
        
        while q:
            curr_node , dis = heapq.heappop(q)
        
            for v, cost in graph[curr_node]:
                curr_dist = dis + cost
                if curr_dist < dist[v]:
                    dist[v] = curr_dist
                    heapq.heappush(q,(v,curr_dist))
        max_time = max(dist[1:])  
        return max_time if max_time != float('inf') else -1 