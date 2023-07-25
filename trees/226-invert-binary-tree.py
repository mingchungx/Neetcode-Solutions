class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        dummy = root

        def invertNode(node: TreeNode) -> None:
            if not node:
                return
            node.left, node.right = node.right, node.left
            invertNode(node.left)
            invertNode(node.right)

        invertNode(root)

        return dummy