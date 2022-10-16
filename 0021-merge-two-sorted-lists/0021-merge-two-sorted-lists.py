# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not (l1 or l2):
            return None
        new_list = ListNode()
        output = new_list
        while l1 or l2:
            if l1 and l2: 
                if l1.val <l2.val:
                    new_list.val = l1.val
                    l1 = l1.next
                else:
                    new_list.val = l2.val
                    l2 = l2.next
            elif l1:
                new_list.val = l1.val
                l1 = l1.next
            else:
                new_list.val = l2.val
                l2 = l2.next
            if l1 or l2:
                new_list.next = ListNode()
                new_list = new_list.next
            
        return output
        