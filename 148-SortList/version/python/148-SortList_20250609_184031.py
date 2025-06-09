# Last updated: 6/9/2025, 6:40:31 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(left,right):
            dummy = ListNode(-1)
            temp = dummy
            while left and right :
                if left.val <= right.val:
                    temp.next = left
                    left = left.next
                else:
                    temp.next = right
                    right = right.next
                temp = temp.next
            while left:
                temp.next = left
                left = left.next
                temp = temp.next
            while right:
                temp.next = right
                right = right.next
                temp = temp.next
            return dummy.next

            
        def findMiddle(head):
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        if not head or head.next is None:
            return head
        middle = findMiddle(head)
        leftHead = head
        rightHead = middle.next
        middle.next = None
        leftHead = self.sortList(leftHead)
        rightHead = self.sortList(rightHead)
        return merge(leftHead , rightHead)
