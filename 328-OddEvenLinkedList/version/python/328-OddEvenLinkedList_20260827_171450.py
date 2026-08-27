# Last updated: 8/27/2026, 5:14:50 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        if not head:
9            return None
10        odd = head
11        even = head.next
12        evenStart = head.next
13        while even and even.next:
14            odd.next = even.next
15            odd = odd.next
16            even.next =odd.next
17            even = even.next
18        odd.next = evenStart
19        return head