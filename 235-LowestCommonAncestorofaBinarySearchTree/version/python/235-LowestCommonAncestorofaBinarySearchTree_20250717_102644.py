# Last updated: 7/17/2025, 10:26:44 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None or root == p or root == q:
            return root
        leftRoot = self.lowestCommonAncestor(root.left,p,q)
        rightRoot = self.lowestCommonAncestor(root.right,p,q)

        if leftRoot == None:
            return rightRoot
        elif rightRoot == None:
            return leftRoot
        else:
            return root
        
