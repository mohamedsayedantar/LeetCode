# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 1
        node = head
        if head.next==None:
            return head
        while head.next:
            length += 1
            head = head.next
        
        if length%2==0:
            length = (length/2)+1
        else:
            length = (length+1)/2
        
        counter = 1
        while node.next:
            counter += 1
            node = node.next
            if counter == int(length):
                return node