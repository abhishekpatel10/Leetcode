# Last updated: 6/8/2025, 11:55:18 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        
        d = deque()
        d.append(root)
        while d:
            same_level = []
            for i in range(len(d)):
                curr = d.popleft()
                same_level.append(curr.val)
                if curr.left:
                    d.append(curr.left)
                if curr.right:
                    d.append(curr.right)
            ans.append(same_level)
                
        return ans
