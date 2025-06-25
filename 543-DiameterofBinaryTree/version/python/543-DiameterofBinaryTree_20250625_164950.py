# Last updated: 6/25/2025, 4:49:50 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia = [0]
        def height(root):

            if not root:
                return 0
            left = height(root.left)
            right = height(root.right)
            dia[0] = max(dia[0], left + right)
            return 1 + max(left,right)
        height(root)
        return dia[0]
        