# Last updated: 9/27/2025, 3:00:19 PM
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
        if root.val == key:
            return self.buildTree(root)
        curr = root
        while curr:
            if curr.val > key:
                if curr.left is not None and curr.left.val == key:
                    curr.left = self.buildTree(curr.left)
                else:
                    curr = curr.left
            else:
                if curr.right is not None and curr.right.val == key:
                    curr.right = self.buildTree(curr.right)
                else:
                    curr = curr.right
        return root
    def buildTree(self,node):
        if not node.right:
            return node.left
        if not node.left:
            return node.right
        rightChild = node.right
        lastright = self.findRight(node.left)
        lastright.right = rightChild
        return node.left
    def findRight(self,node):
        if node.right == None:
            return node
        return self.findRight(node.right)
            