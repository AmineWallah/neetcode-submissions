# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        temp = root
        
        while temp:
            if temp.val > p.val and temp.val > q.val:
                temp = temp.left
            elif temp.val < p.val and temp.val < q.val:
                temp = temp.right
            else:
                return temp
