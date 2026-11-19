# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        # Brute force solution
        from collections import deque
        q = deque([root])
        values = [root.val]
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    if node.left:
                        q.append(node.left)
                        values.append(node.left.val)
                    if node.right:
                        q.append(node.right)
                        values.append(node.right.val)

        values = sorted(values)
        
        return values[k - 1]