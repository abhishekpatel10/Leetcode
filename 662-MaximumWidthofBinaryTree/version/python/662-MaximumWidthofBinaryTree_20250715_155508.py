# Last updated: 7/15/2025, 3:55:08 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()
        if not root:
            return 0
        q.append((root,0))
        ans = 0
        while q:
            n = len(q)
            _,curr_min = q[0]
            for _ in range(n):
                curr_node , prev_min = q.popleft()
                index = prev_min - curr_min
                if curr_node.left:
                    q.append((curr_node.left,2*index + 1))
                if curr_node.right:
                    q.append((curr_node.right,2*index + 2))
            current_width = q[-1][1] - q[0][1] + 1 if q else 1
            ans = max(ans, current_width)
        return ans