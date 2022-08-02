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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        output = head
        my_list = []
        if not head:
            return None
        my_list.append(head.val)
        while head.next:
            head = head.next
            my_list.append(head.val)
        
        print(my_list)
        
        for i in my_list[::-1]:
            node.val = i
            node = node.next
            
        return output
        