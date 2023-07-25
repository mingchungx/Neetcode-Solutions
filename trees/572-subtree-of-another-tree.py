class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def traverse(root, subRoot):            
            if not (root and subRoot):
                return root is subRoot
            return root.val == subRoot.val and traverse(root.left, subRoot.left) and traverse(root.right, subRoot.right)
        if traverse(root, subRoot):
            return True
        if not root:
            return False
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)