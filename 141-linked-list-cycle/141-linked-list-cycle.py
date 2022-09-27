# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        fast, slow = head, head
        
        # while fast node and fast pointer aren't null
        while fast and fast.next:
            # shift fast pointer by 2
            fast = fast.next.next
            # shift slow pointer by 1
            slow = slow.next
            # if fast pointer catches up to slow pointer, there's a cycle in the LL
            if fast == slow:
                return True
        # if fast node and its pointer ever equal null, that means there's a dead end
        # there's no cycle
        return False