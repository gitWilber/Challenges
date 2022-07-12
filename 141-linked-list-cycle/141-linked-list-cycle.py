# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        
        # While fast pointer is not null
        while fast and fast.next:
            # iterate slow pointer by 1
            slow = slow.next
            # iterate fast pointer by 2
            fast = fast.next.next
            # if both pointers meet/ equal to the same node, return true
            if fast == slow:
                return True
        # if the fast pointer does equal to null that means there is no loop.
        # the list stops
        return False
    
        # To determine a cycle in a linked list, we can use two pointers
        # One pointer is at the head, and the other is ahead by two
        # If both pointers ever equal to each other, that must mean there is a cycle
        # Becaue the second pointer cycled and went back
        # Floyd's Tortoise and Hare Algorithm