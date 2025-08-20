# Last updated: 8/20/2025, 4:36:57 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root,summ):
            if not root:
                return False
            if not root.left and not root.right:
                return root.val == summ
            left = dfs(root.left,summ - root.val)
            right = dfs(root.right,summ - root.val)
            return left or right
        return dfs(root,targetSum)
        