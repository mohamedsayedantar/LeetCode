# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        self.state = True
        def checkMirror(root1, root2):
            if root1 and root2 and self.state:
                if root1.val != root2.val:
                    self.state=False
                    return
                else:
                    checkMirror(root1.left, root2.right)
                    checkMirror(root1.right, root2.left)
            elif root1 or root2:
                self.state = False
            else:
                pass
            
        checkMirror(root.left, root.right)
        return self.state