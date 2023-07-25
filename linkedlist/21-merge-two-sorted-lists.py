class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = cur = ListNode()
        node1, node2 = list1, list2

        while (node1 and node2):
            if node1.val == node2.val:
                # Take from list1
                cur.next = ListNode(node1.val)
                node1 = node1.next
            else:
                # Take from the smallest of list1 and list2
                if node1.val < node2.val:
                    cur.next = ListNode(node1.val)
                    node1 = node1.next
                else:
                    cur.next = ListNode(node2.val)
                    node2 = node2.next
            cur = cur.next

        # Now check the larger of the two list lengths
        while (node1 and not node2):
            cur.next = ListNode(node1.val)
            node1 = node1.next
            cur = cur.next
        while (node2 and not node1):
            cur.next = ListNode(node2.val)
            node2 = node2.next
            cur = cur.next
            
        return dummy.next