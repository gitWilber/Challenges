# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        curr = head
        
        # while theres a current node
        while(curr):
            
            # temp hold next value before we switch pointer
            temp = curr.next
            # current pointer will point to prev
            curr.next = prev
            # iterate, prev is now curr node
            prev = curr
            # iterate, curr node goes to temp node, which has next node stored
            curr = temp
        
        # return reverse LL
        return prev
