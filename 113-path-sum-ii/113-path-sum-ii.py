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
            #print(root.val, path)
            if root:
                if root.left or root.right:
                    path += str(root.val) + " "
                    #print(path)
                    sum_path(root.left, path)
                    sum_path(root.right, path)
                else:
                    path += str(root.val) + " "
                    #print("hereeeee", path.split())
                    list1 = []
                    for i in path.split():
                        list1.append(int(i))
                    if sum(list1)==targetSum:
                        #print("kkkk", sum(list1))
                        self.paths.append(list1)
                    
        sum_path(root, "")
        return self.paths