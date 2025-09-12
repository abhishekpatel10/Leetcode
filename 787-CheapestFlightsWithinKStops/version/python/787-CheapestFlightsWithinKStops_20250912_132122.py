# Last updated: 9/12/2025, 1:21:22 PM
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,cost in flights:
            graph[u].append((v,cost))
        print(graph)

        dist = [float('inf')] * n
        dist[src] = 0
        heap = [(0,src,0)]

        while heap:
            stops, curr_node,curr_cost = heapq.heappop(heap)
            if stops > k:
                continue
            for nei,cost in graph[curr_node]:
                new_cost = curr_cost + cost
                if new_cost < dist[nei]:
                    dist[nei] = new_cost
                    heapq.heappush(heap,(stops+1,nei,new_cost))
        if dist[dst] != float('inf'):
            return dist[dst]
        else:
            return -1