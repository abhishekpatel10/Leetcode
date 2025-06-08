# Last updated: 6/8/2025, 11:55:03 AM
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        otn={}
        curr = head
        while curr:
            node = Node(x=curr.val)
            otn[curr] = node
            curr = curr.next
        curr = head
        while curr:
            new_node = otn[curr]
            new_node.next = otn[curr.next] if curr.next else None
            new_node.random = otn[curr.random] if curr.random else None
            curr = curr.next
        return otn[head]
        