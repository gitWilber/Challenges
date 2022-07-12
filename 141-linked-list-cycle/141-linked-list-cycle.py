# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # To determine a cycle in a linked list, we can use two pointers
        # One pointer is at the head, and the other is ahead by two
        # If both pointers ever equal to each other, that must mean there is a cycle
        # Becaue the second pointer cycled and went back
        # Floyd's Tortoise and Hare Algorithm
        
        slow, fast = head, head
        
        # While second pointer is not null
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if fast == slow:
                return True
        return False