class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(left, right):
            if not left and not right:
                return True
            elif (left and not right) or (right and not left):
                return False
            else:
                return left.val == right.val and isMirror(left.left, right.right) and isMirror(left.right, right.left)
        return isMirror(root.left, root.right)