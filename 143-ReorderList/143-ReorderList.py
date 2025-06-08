# Last updated: 6/8/2025, 11:55:01 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        currentNode = head
        temp = []
        temp2 = []
        while currentNode.next:
            temp.append(currentNode)
            currentNode = currentNode.next
        temp.append(currentNode)

        if len(temp)%2 == 0:
            count = int(len(temp)/2)
        else:
            count = int((len(temp)+1)/2)
        
        for i in range(0,count):
            temp2.append(temp[i])
            if len(temp)%2 == 0:
                if count != i:
                    temp2.append(temp[-1*(i+1)])
            else:
                if count -1 != i:
                    temp2.append(temp[-1*(i+1)])
        
        for i in range(len(temp2)):
            if len(temp2)-1 != i:
                temp2[i].next = temp2[i+1]
            else:
                temp2[i].next = None