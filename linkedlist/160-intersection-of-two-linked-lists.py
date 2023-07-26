class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b = headA, headB

        while (a != b):
            if a:
                a = a.next
            else:
                a = headB
            if b:
                b = b.next
            else:
                b = headA

        # We know either they are the same or no result
        return a
