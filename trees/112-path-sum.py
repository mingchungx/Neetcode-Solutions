class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:

        def dfs(node, curSum):
            # Base case
            if not node:
                return False
            
            curSum += node.val
            
            # at leaf node
            if not node.left and not node.right:
                return curSum == targetSum
            
            return dfs(node.left, curSum) or dfs(node.right, curSum)
        
        return dfs(root, 0)