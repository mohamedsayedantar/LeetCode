# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        head1 = head
        arr = []
        while head1:
            arr.append(head1.val)
            head1 = head1.next
            
            
        #print(arr)
        head1 = head
        while head1:
            #print(head1.val, arr[-1])
            if head1.val != arr.pop(-1):
                #print(head1.val, arr)
                return False
            head1 = head1.next
            
        return True 