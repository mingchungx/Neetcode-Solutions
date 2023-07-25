class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # We can use a dummy node and two pointers
        # The second pointer is exactly n indexes away from first
        dummy = ListNode(0, head)
        first = dummy
        second = head

        # This will never go "out of bounds" because of the condition that 1 <= n <= sz
        for _ in range(n):
            second = second.next
        
        # Now we shift both first and second
        while (second):
            first = first.next
            second = second.next
        
        first.next = first.next.next

        return dummy.next