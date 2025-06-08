# Last updated: 6/8/2025, 11:52:30 AM
from heapq import heappop, heappush
from collections import defaultdict
from typing import List

MOD = 10**9 + 7

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # Step 1: Build the Graph
        adj = defaultdict(list)
        MOD = 10**9 + 7
        for u, v, cost in roads:
            adj[u].append((v, cost))
            adj[v].append((u, cost))

        # Step 2: Initialize distance and ways array
        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0  # Distance from node 0 to itself is 0
        ways[0] = 1  # Only one way to start at node 0

        # Step 3: Min-Heap for Dijkstra's Algorithm
        min_heap = [(0, 0)]  # (cost, node)
        
        while min_heap:
            cost , curr_node = heappop(min_heap)
            for nei,weight in adj[curr_node]:
                curr_cost = cost + weight
                if curr_cost < dist[nei]:
                    dist[nei] = curr_cost
                    ways[nei] = ways[curr_node]
                    heappush(min_heap,(curr_cost,nei))
                elif curr_cost == dist[nei]:
                    ways[nei] = (ways[nei] + ways[curr_node]) % MOD 
        return ways[n-1] 