# Last updated: 6/8/2025, 11:54:58 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        curr = head
        curr1 = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        i = 0
        arr.sort()
        while head:
            head.val = arr[i]
            i += 1
            head = head.next
        return curr1

