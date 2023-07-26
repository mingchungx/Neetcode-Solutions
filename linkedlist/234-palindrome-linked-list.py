class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # Get the midpoint
        first, slow, fast = head, head, head

        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        
        cur = slow
        prev = None

        while (cur):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        second = prev

        # Check if second and first are the same
        while (first and second):
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True

