class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        # If the BST was actually a sorted list, you would just compare neighbouring difference
        # Since the BST has its own sorting property, you can use it to also compare neighbouring differences
        # Compare the node to left and right
        # Keep track of the previous node (the neighbour of the current)

        prev, minDiff = None, float('inf')

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nonlocal prev, minDiff
            if prev:
                minDiff = min(minDiff, abs(node.val - prev.val))
            prev = node
            dfs(node.right)

        dfs(root)
        return minDiff