# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def cal_dep(node):
            if node:
                return max(cal_dep(node.left), cal_dep(node.right)) + 1
            else:
                return 0
        return cal_dep(root)