# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        dict1 = {}
        
        def nums(node):
            if node:
                dict1[node.val] = 1
                nums(node.left)
                nums(node.right)
                
        nums(root)
        print(dict1)
        
        for i in dict1:
            dict1[i] = 0
            if k-i in dict1:
                if dict1[k-i] == 1:
                    return True 
            
                