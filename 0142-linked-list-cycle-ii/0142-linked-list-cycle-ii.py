# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        node_list = []
        if head==None:
            return None
        #node_list.append(head)
        while head.next:
            node_list.append(head)
            head = head.next
            if head in node_list:
                return head
            
        return None