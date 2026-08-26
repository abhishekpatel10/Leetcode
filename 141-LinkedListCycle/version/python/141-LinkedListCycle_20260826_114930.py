# Last updated: 8/26/2026, 11:49:30 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def hasCycle(self, head: Optional[ListNode]) -> bool:
9        dummy = ListNode()
10        dummy.next = head
11        slow = fast = dummy
12
13        while fast and fast.next:
14            fast = fast.next.next
15            slow = slow.next
16            if slow == fast:
17                return True
18        
19        return False
20        