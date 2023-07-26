class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow, fast = head, head.next

        while (fast):
            # If fast.next does not exist, then there must be even number of elements
            if not fast.next:
                return slow.next
            if fast.next:
                slow = slow.next
                fast = fast.next.next

        return slow