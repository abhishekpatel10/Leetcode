# Last updated: 8/31/2026, 4:03:07 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        if not head or head.next is None:
9            return head
10        middle = self.middle(head)
11        leftside = head
12        rightside = middle.next
13        middle.next = None
14        left = self.sortList(leftside)
15        right = self.sortList(rightside)
16        return self.merge(left,right)
17
18    def merge(self,left,right):
19            dummy = ListNode(-1)
20            temp = dummy
21            while left and right :
22                if left.val <= right.val:
23                    temp.next = left
24                    left = left.next
25                else:
26                    temp.next = right
27                    right = right.next
28                temp = temp.next
29            while left:
30                temp.next = left
31                left = left.next
32                temp = temp.next
33            while right:
34                temp.next = right
35                right = right.next
36                temp = temp.next
37            return dummy.next
38
39    def middle(self,node):
40        slow = node
41        fast = node.next
42        while fast and fast.next:
43            slow = slow.next
44            fast = fast.next.next
45        return slow