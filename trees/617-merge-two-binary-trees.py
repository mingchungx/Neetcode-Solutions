class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1 and not root2:
            return None
        elif root1 and not root2:
            return root1
        elif root2 and not root1:
            return root2
        else:
            return TreeNode(
                val=root1.val + root2.val,
                left=self.mergeTrees(root1.left, root2.left),
                right=self.mergeTrees(root1.right, root2.right)
            )