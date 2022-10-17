"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        output = []
        
        def get_pre(node):
            output.append(node.val)
            for nod in node.children:
                get_pre(nod)
        if root is None:
            return output
        get_pre(root)
        return output