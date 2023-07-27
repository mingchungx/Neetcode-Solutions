class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        if not root:
            return []

        output = []

        def traverse(node):
            if not node:
                return
            output.append(node.val)
            traverse(node.left)
            traverse(node.right)
        
        traverse(root)
        
        return output