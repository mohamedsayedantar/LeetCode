# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.out = True
        
        def isvalid(node, minimum, maximum):
            if node.left:
                if node.left.val >= node.val:
                    self.out = False
                if minimum:
                    if node.left.val <= minimum:
                        self.out = False
                isvalid(node.left, minimum, node.val)
            if node.right:
                if node.right.val <= node.val:
                    self.out = False
                if maximum:
                    if node.right.val >= maximum:
                        self.out = False
                isvalid(node.right, node.val, maximum)
            
        isvalid(root, None, None)
        return self.out