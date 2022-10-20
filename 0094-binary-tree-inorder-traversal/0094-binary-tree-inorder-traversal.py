# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out_list = []
        def get_inorder(root):
            if root:
                get_inorder(root.left)
                out_list.append(root.val)
                get_inorder(root.right)
        get_inorder(root)
        return out_list