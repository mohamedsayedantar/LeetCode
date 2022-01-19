# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.state = False
        def sum_path(root, sum1):
            if root:
                if root.left or root.right:
                    #sum1 += root.val
                    sum_path(root.left, sum1+root.val)
                    sum_path(root.right, sum1+root.val)
                else:
                    sum1 += root.val
                    if sum1==targetSum:
                        self.state = True
                    
        sum_path(root, 0)
        return self.state
