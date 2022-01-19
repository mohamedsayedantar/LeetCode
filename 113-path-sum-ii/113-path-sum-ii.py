# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.paths = []
        def sum_path(root, path):
            if root:
                if root.left or root.right:
                    #path += str(root.val) + " "
                    sum_path(root.left, path+ str(root.val) + " ")
                    sum_path(root.right, path+ str(root.val) + " ")
                else:
                    path += str(root.val) + " "
                    list1 = []
                    for i in path.split():
                        list1.append(int(i))
                    if sum(list1)==targetSum:
                        self.paths.append(list1)
                    
        sum_path(root, "")
        return self.paths