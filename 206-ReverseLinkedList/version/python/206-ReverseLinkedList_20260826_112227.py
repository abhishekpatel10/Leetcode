# Last updated: 8/26/2026, 11:22:27 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        prev = None
9        curr = head
10        while curr:
11            temp = curr.next
12            curr.next = prev
13            prev = curr
14            curr = temp
15        return prev