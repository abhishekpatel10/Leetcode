# Last updated: 6/21/2025, 11:13:03 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getKthNode(temp,k):
            k -=1
            while k > 0 and temp:
                k -=1
                temp = temp.next
            return temp
        def reverse(temp):
            curr = temp
            prev = None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        temp = head
        prevNode = None
        while temp:
            kthNode = getKthNode(temp,k)
            if kthNode is None:
                if prevNode:
                    prevNode.next = temp
                break
            nextgroup = kthNode.next
            kthNode.next = None
            reverse(temp)
            if head == temp:
                head = kthNode
            else:
                prevNode.next = kthNode
            
            prevNode = temp
            
            temp = nextgroup
        return head
        