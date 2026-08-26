# Last updated: 8/26/2026, 11:50:13 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def hasCycle(self, head: Optional[ListNode]) -> bool:
9        if pos == -1:
10            return False
11        fast = head
12        slow = head
13        while fast and fast.next:
14            slow = slow.next
15            fast = fast.next.next
16            if slow == fast:
17                return True
18        return False