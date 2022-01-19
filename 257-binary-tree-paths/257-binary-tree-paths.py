# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.paths = []
        def sum_path(root, path):
            if root:
                if root.left or root.right:
                    sum_path(root.left, path+ str(root.val) + "->")
                    sum_path(root.right, path+ str(root.val) + "->")
                else:
                    path += str(root.val)                    
                    self.paths.append(path)
                    
        sum_path(root, "")
        return self.paths