# Last updated: 8/26/2026, 12:32:32 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
9        fast = head
10        slow = head
11        temp = None
12        while fast and fast.next:
13            slow = slow.next
14            fast = fast.next.next
15            if slow == fast:
16                slow = head
17                while fast and slow:
18                    if slow == fast:
19                        return slow
20                    slow = slow.next
21                    fast = fast.next
22                    
23        return None