# Last updated: 9/23/2025, 12:21:48 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque()
        q.append((root,0))
        ans = float('-inf')
        while q:
            n = len(q)
            _, prev_min = q[0]
            for _ in range(n):
                node , curr_min = q.popleft()
                index = curr_min - prev_min
                if node.left:
                    q.append((node.left,2*index + 1))
                if node.right:
                    q.append((node.right,2*index + 2))
            current_width = q[-1][1] - q[0][1] + 1 if q else 1
            ans = max(current_width,ans)
        return ans