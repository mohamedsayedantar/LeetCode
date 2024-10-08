# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out_list = []
        def get_postorder(root):
            if root:
                get_postorder(root.left)
                get_postorder(root.right)
                out_list.append(root.val)
                
        get_postorder(root)
        return out_list