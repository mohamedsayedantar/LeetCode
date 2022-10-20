# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out_list = []
        def get_preorder(root):
            if root:
                out_list.append(root.val)
                get_preorder(root.left)
                get_preorder(root.right)
                
        get_preorder(root)
        return out_list