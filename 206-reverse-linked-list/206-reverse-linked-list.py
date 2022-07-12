# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        
        
        # Use two pointers, a previous and current pointer
        # current pointer will point to previous
        
        # Loop, while curr is not null, we can switch pointers and iterate
        while curr:
            # Use a temp node to point current value to right, so we can iterate once we switch pointers
            tempNext = curr.next
            # point node to previous node
            curr.next = prev
            # shift previous node to equal to current node
            prev = curr
            # shift current node to temp next node which is to the right
            curr = tempNext
        
        return prev