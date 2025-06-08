# Last updated: 6/8/2025, 11:55:05 AM
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        start = node
        stk = [start]
        o_to_n = {}
        visited = set()
        visited.add(start)
        while stk:
            node = stk.pop()
            o_to_n[node] = Node(val = node.val)

            for nei in node.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    stk.append(nei)
        for old , new in o_to_n.items():
            for nei in  old.neighbors:
                new_nei = o_to_n[nei]
                new.neighbors.append(new_nei)
        return o_to_n[start]