class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameter = [0]

        def dfs(node):
            # This function gets the height
            if not node:
                return -1 # This is to make the math work out correctly
            left = dfs(node.left)
            right = dfs(node.right)

            diameter[0] = max(diameter[0], 2 + left + right)

            return 1 + max(left, right)
        
        dfs(root)

        return diameter[0]