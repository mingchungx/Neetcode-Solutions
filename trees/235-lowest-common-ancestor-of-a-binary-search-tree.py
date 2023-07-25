class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while (root):
            # If both are smaller, search left
            if p.val < root.val and q.val < root.val:
                root = root.left
            # If both are larger, search right
            elif p.val > root.val and q.val > root.val:
                root = root.right
            # Otherwise we have found
            else:
                return root
        return None