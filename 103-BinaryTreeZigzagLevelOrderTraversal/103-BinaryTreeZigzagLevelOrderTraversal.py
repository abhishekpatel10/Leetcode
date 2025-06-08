# Last updated: 6/8/2025, 11:55:17 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        if not root:return []
        q.append(root)
        ans = []
        lefttoright = True
        while q:
            size = len(q)
            curr_lvl = [0]*size
            for i in range(len(q)):
                node = q.popleft()
                index = i if  lefttoright else (size-i-1)
                curr_lvl[index] = node.val
                if node.left : q.append(node.left)
                if node.right : q.append(node.right)
            ans.append(curr_lvl)
            lefttoright = not lefttoright
        return ans