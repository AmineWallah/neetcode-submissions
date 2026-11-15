# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, mx):
            if not root: return 0
            good = 1 if root.val >= mx else 0
            mx = max(mx, root.val)
            return good + dfs(root.left, mx) + dfs(root.right, mx)

        return dfs(root, float('-inf'))