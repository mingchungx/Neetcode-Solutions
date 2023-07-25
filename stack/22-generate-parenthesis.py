class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        # If left < n: Add (
        # If right < left: Add )
        # End: left == right == n

        stack = []
        output = []

        def backtrack(left: int, right: int):
            if left == right == n:
                output.append("".join(stack))
                return
            if left < n:
                stack.append("(")
                backtrack(left + 1, right)
                # We have explored all possibilities with the above ( added, so we backtrack by popping
                stack.pop()
            if right < left:
                stack.append(")")
                backtrack(left, right + 1)    
                stack.pop()
        
        backtrack(0, 0)
        
        return output