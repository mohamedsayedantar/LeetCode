# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sums = 0
        def sumleaves(root, state):
            if root:
                if state=="left":
                    if not(root.left or root.right):
                        self.sums += root.val
                sumleaves(root.left, "left")
                sumleaves(root.right, "right")
            
        
        sumleaves(root, "root")
        return self.sums
        