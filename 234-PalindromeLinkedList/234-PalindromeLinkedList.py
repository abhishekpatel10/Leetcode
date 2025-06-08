# Last updated: 6/8/2025, 11:54:37 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(head: Optional[ListNode]):
            prev = None
            while head:
                front = head.next
                head.next = prev
                prev = head
                head = front
            return prev

        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        secondHead = reverse(slow.next)
        while secondHead:
            if secondHead.val != head.val:
                reverse(secondHead)
                return False
            head = head.next
            secondHead = secondHead.next
        reverse(secondHead)
        return True
