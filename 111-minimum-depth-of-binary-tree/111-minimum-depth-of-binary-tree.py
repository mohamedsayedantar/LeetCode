# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        self.depth = -1
        if not root:
            return 0
        def cal_dep(node, d):
            if node:
                if node.left or node.right:
                    cal_dep(node.left, d+1)
                    cal_dep(node.right, d+1)
                else:
                    if self.depth == -1:
                        self.depth = d
                    else:
                        if d<self.depth:
                            self.depth = d
            
        cal_dep(root, 1)
        return self.depth