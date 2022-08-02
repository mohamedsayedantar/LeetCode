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
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        new_lnkdlist = ListNode("")
        linked = new_lnkdlist
        state = True
        if not head:
            return linked
        while state:
            #print(head.val)
            if head.val == val:
                pass
            else:
                if new_lnkdlist.val=="":
                    new_lnkdlist.val = head.val
                else:
                    new_lnkdlist.next = ListNode()
                    new_lnkdlist = new_lnkdlist.next
                    new_lnkdlist.val = head.val
                
                #print("new: ", new_lnkdlist.val)
                #if head.next:
                    #new_lnkdlist.next = ListNode()
                    #new_lnkdlist = new_lnkdlist.next
            head = head.next
            if head==None:
                state = False
            
        return linked
        
        