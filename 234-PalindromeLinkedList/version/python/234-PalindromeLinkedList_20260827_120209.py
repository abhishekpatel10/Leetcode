# Last updated: 8/27/2026, 12:02:09 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def isPalindrome(self, head: Optional[ListNode]) -> bool:
8        slow = fast = head
9        while fast.next and fast.next.next is not None:
10            slow = slow.next
11            fast = fast.next.next
12        newHead = self.reverse(slow.next)
13        curr_head = head
14
15        while newHead:
16            if newHead.val != curr_head.val:
17                self.reverse(newHead)
18                return False
19            curr_head = curr_head.next
20            newHead = newHead.next
21        self.reverse(newHead)
22        return True
23    
24    def reverse(self,node):
25        prev = None
26        first = node
27        while first:
28            temp = first.next
29            first.next = prev
30            prev = first
31            first = temp
32        return prev