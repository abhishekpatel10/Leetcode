# Last updated: 8/28/2026, 4:57:38 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
8        d = ListNode()
9        d.next = head
10        fast = d
11        slow = d
12        for _ in range(n+1):
13            fast = fast.next
14        while fast:
15            slow  = slow.next
16            fast = fast.next
17        slow.next = slow.next.next
18        return d.next
19        