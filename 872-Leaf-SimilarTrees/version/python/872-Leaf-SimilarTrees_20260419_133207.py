# Last updated: 4/19/2026, 1:32:07 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
9        def collect_leaf_values(root, leaf_values):
10            if not root:
11                return
12            if not root.left and not root.right:
13                leaf_values.append(root.val)
14            collect_leaf_values(root.left, leaf_values)
15            collect_leaf_values(root.right, leaf_values)
16
17        leaf_values1 = []
18        leaf_values2 = []
19
20        collect_leaf_values(root1, leaf_values1)
21        collect_leaf_values(root2, leaf_values2)
22
23        return leaf_values1 == leaf_values2
24    
25