# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None:
            return None
        while head.next:
            head.val = "v"
            head = head.next
            if head.val == "v":
                return True
        return False
        