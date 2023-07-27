class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        if not root:
            return []

        output = []

        def traverse(node):
            if not node:
                return
            traverse(node.left)
            output.append(node.val)
            traverse(node.right)

        traverse(root)

        return output