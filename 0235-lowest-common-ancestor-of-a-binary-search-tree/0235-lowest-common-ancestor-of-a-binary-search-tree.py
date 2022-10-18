# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        arr1 = []
        arr2 = []
        
        def get_arr(node, target, arr):
            if node:
                arr.append(node)
                if node == target:
                    return 
                elif target.val > node.val:
                    get_arr(node.right, target, arr)
                else:
                    get_arr(node.left, target, arr)
        
        get_arr(root, p, arr1)
        #print(arr1)
        get_arr(root, q, arr2)
        #print(arr2)
        
        shared, L = None, None
        L1, L2 = len(arr1), len(arr2)
        if L1>L2:
            L = L2
        else:
            L = L1
        
        
        for i in range(L):
            #print(i)
            if arr1[i] == arr2[i]:
                shared = arr1[i]
                #print ("shared = ", shared)
            else:
                #print("ff")
                return shared
                
        return shared
        
        