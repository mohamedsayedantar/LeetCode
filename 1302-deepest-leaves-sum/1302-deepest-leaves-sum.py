# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def cal_dep(node):
            if node:
                return max(cal_dep(node.left), cal_dep(node.right)) + 1
            else:
                return 0
            
        depth = cal_dep(root)
        self.sum1 = 0
        def deep(root, level):
            if root:
                if level==depth:
                    self.sum1 += root.val
                    return
                deep(root.left, level+1)
                deep(root.right, level+1)
        deep(root, 1)        
        return self.sum1
