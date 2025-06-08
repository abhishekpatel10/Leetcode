# Last updated: 6/8/2025, 11:53:20 AM
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,cost in flights:
            adj[u].append((v,cost))
        row = len(flights)
        col = len(flights[0])
        dist = [float('inf')]* n
        q = deque()
        q.append((0,src,0))
        dist[src] = 0
        while q:
            stops, curr_node,curr_cost = q.popleft()
            
            if stops > k:
                continue
            for nei,weight in adj[curr_node]:
                new_cost = curr_cost + weight
                if new_cost < dist[nei]:
                    dist[nei] = new_cost
                    q.append((stops+1,nei,new_cost))
        return dist[dst] if dist[dst] != float('inf') else -1 
