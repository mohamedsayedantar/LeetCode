# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.output = None 
        def get_n(node, value):
            if node:
                if node.val == value:
                    self.output = node
                else:
                    get_n(node.right, value)
                    get_n(node.left, value)
                    
        get_n(root, val)
        return self.output