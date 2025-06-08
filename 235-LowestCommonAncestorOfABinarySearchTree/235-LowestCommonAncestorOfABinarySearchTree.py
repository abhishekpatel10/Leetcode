# Last updated: 6/8/2025, 11:54:35 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = [root]

        def search(root):
            if not root:
                return
            
            lca[0] = root
            if root is p or root is q:
                return
            elif  p.val > root.val and q.val > root.val:
                return search(root.right)
            elif  p.val < root.val and q.val < root.val:
                return search(root.left)
            else:
                return
        search(root)
        return lca[0]
