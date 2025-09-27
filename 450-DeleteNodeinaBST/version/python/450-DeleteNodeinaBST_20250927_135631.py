# Last updated: 9/27/2025, 1:56:31 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        curr = root
        if root.val == key:
            return self.buildTree(root)
        dummy = root
        curr = root
        while curr:
            if curr.val > key:
                if curr.left and curr.left.val == key:
                    curr.left = self.buildTree(curr.left)
                    break
                else:
                    curr = curr.left
            elif curr.val < key:
                if curr.right and curr.right.val == key:
                    curr.right = self.buildTree(curr.right)
                    break
                else:
                    curr = curr.right
            else:
                break
        return dummy


    def buildTree(self,node):
        if not node.left:
            return node.right
        if not node.right:
            return node.left
        # both children exist
        rightChild = node.right
        lastRight = self.findRight(node.left)
        lastRight.right = rightChild
        return node.left
    def findRight(self, node: TreeNode) -> TreeNode:
        while node.right:
            node = node.right
        return node

