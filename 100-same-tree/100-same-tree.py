# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.state = True
        def convertToList1(root1, root2):
            if root1 and root2 and self.state:
                if root1.val != root2.val:
                    self.state=False
                    return
                else:
                    convertToList1(root1.left, root2.left)
                    convertToList1(root1.right, root2.right)
            elif root1 or root2:
                self.state = False
            else:
                pass
        
                
       
        convertToList1(p, q)
        #print(self.list1, self.list2)
        return self.state