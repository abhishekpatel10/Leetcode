# Last updated: 10/6/2025, 11:28:18 AM
import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        
        # Initialize effort grid with infinity
        effort = [[float('inf')] * col for _ in range(row)]
        effort[0][0] = grid[0][0]  # Set initial effort to grid[0][0]

        # Min-heap to store (effort, row, col)
        heap = [(grid[0][0], 0, 0 )]  # Start with grid[0][0] effort
        
        while heap:
            min_eff, r, c = heapq.heappop(heap)

            # If we reach bottom-right, return the effort
            if r == row - 1 and c == col - 1:
                return min_eff

            # Explore all 4 possible moves
            dirs = [(0,1), (1,0), (-1,0), (0,-1)]
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col:
                    # Calculate the new max effort needed
                    curr_eff = grid[nr][nc]
                    maxeffort = max(curr_eff, min_eff)

                    if maxeffort < effort[nr][nc]:
                        effort[nr][nc] = maxeffort
                        heapq.heappush(heap, (maxeffort, nr, nc))

        return -1  # Should never be reached
