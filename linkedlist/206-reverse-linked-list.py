class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, cur = None, head
        while (cur):
            # Keep the next pointer
            next = cur.next

            # Swap the pointer direction
            cur.next = prev

            # Keep track of previous node
            prev = cur

            # Go to next node
            cur = next
        
        return prev
        