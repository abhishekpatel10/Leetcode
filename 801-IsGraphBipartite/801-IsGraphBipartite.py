# Last updated: 6/8/2025, 11:53:20 AM
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n  # 0 means "uncolored"
        
        for i in range(n):
            if color[i] == -1:  # If not colored
                if not self.dfs(i, graph, color, 0):  # Start with color 1
                    return False
        return True

    def dfs(self, node, graph, color, next_color):
        color[node] = next_color  # Assign the current node a color

        for nei in graph[node]:  # Iterate through neighbors
            if color[nei] == -1:  # If neighbor is uncolored
                if not self.dfs(nei, graph, color, 1 - color[node]):  # Alternate color
                    return False
            elif color[nei] == color[node]:  # If neighbor has the same color, graph is not bipartite
                return False
        return True
