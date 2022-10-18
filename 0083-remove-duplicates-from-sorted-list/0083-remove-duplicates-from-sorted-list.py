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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        output = head
        if head==None:
            return None
        elif head.next==None:
            return head
        else:
            last = head.val
            while head.next:
                if head.next.val == last:
                    if head.next.next==None:
                        head.next = None
                        break
                    else:
                        head.next = head.next.next
                        
                else:
                    head = head.next
                    last = head.val
                    #print("head.next:", head.next, last)
                    
                
            return output
        