# Last updated: 6/8/2025, 11:55:15 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]
        def dfs(node):
            if not node:
                return True
            maxRight = dfs(node.left)
            maxLeft = dfs(node.right)
            if abs(maxRight - maxLeft) > 1:
                balanced[0] = False
                return 0
            return 1 + max(maxRight,maxLeft)
        dfs(root)
        return balanced[0]
