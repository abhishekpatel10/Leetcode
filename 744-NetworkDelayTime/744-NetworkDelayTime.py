# Last updated: 6/8/2025, 11:53:24 AM
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist  = [float('inf') ]* (n+1)
        adj = defaultdict(list)
        for u ,v ,cost in times:
            adj[u].append((v,cost))
        dist[k] = 0
        min_heap = []
        heappush(min_heap, (0, k))  
        while min_heap:
            cost,curr_node = heappop(min_heap)

            for nei , weight in adj[curr_node]:
                curr_cost = cost + weight
                if curr_cost < dist[nei]:
                    dist[nei] = curr_cost
                    heappush(min_heap,(curr_cost,nei))
        max_time = max(dist[1:])  
        return max_time if max_time != float('inf') else -1 
        
