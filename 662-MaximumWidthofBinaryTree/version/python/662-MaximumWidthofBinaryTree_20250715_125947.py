# Last updated: 7/15/2025, 12:59:47 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append((root,1))
        ans = 0
        while q:
            size = len(q)
            
            _,head_index = q[0]
            for _ in range(size):
                node,index = q.popleft()
                n_index = index - head_index
                if node.left:
                    q.append((node.left,2*n_index + 1))
                if node.right:
                    q.append((node.right,2*n_index+2))
            current_width = q[-1][1] - q[0][1] + 1 if q else 1
            ans = max(ans, current_width)
        return ans
            
            
            

