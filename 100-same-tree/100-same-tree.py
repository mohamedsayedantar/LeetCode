# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.list1 = []
        self.list2 = []
        
        def convertToList1(root):
            if root:
                self.list1.append(root.val)
                convertToList1(root.left)
                convertToList1(root.right)
            else:
                self.list1.append(None)
                
        def convertToList2(root):
            if root:
                self.list2.append(root.val)
                convertToList2(root.left)
                convertToList2(root.right)
            else:
                self.list2.append(None)
                
        convertToList1(p)
        convertToList2(q)
        #print(self.list1, self.list2)
        return self.list1==self.list2