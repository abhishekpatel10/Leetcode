# Last updated: 6/26/2025, 3:35:32 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = defaultdict(lambda: defaultdict(lambda: list()))
        res = []
        if not root:
            return res
        q = deque()
        q.append((root, (0, 0)))
        while q:
            temp ,(x,y) = q.popleft()
            nodes[x][y].append(temp.val)
            if temp.left:
                q.append((temp.left,(x-1,y+1)))
            if temp.right:
                q.append((temp.right,(x+1,y+1)))
        for x in sorted(nodes):  # sort columns
            col = []
            for y in sorted(nodes[x]):  # sort rows within the column
                col.extend(sorted(nodes[x][y]))  # sort multiple nodes at same (x, y)
            res.append(col)

        return res