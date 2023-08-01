class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: TreeNode) -> str:
        output = []

        def preorder(node):
            if not node:
                return
            
            # For every node, it must have a ( preceeding
            output.append("(")
            output.append(str(node.val))

            # Retain "one-to-one" mapping (so all trees are string unique)
            if node.right and not node.left:
                output.append("()")

            # Traverse left and right
            preorder(node.left)
            preorder(node.right)

            # Every node ends with a )
            output.append(")")
    
        preorder(root)

        return "".join(output)[1:-1]