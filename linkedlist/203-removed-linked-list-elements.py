class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # Edge case where there is no val
        if not head:
            return None

        # Consider edge case where the first element is not good
        while (head):
            if head.val == val:
                head = head.next
            else:
                break

        prev = None
        dummy = cur = head

        # Start iterating through LinkedList
        while (cur):
            if cur.val == val:
                # Preform deletion
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        
        return dummy