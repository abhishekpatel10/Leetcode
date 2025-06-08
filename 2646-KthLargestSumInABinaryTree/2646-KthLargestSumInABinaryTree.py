# Last updated: 6/8/2025, 11:52:18 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        d = deque()
        if root:
            d.append(root)
        arr = []
        while d:
            curr_sum = 0
            for _ in range(len(d)):
                curr  = d.popleft()
                curr_sum += curr.val
                if curr.left:d.append(curr.left)
                if curr.right : d.append(curr.right)
            arr.append(curr_sum)
        arr.sort()
        return arr[-k] if k <= len(arr) else -1
