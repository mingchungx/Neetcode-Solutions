class Solution:
    def isValid(self, s: str) -> bool:
        # Create a map 
        ht = {
            "}":"{",
            ")":"(",
            "]":"["
        }

        stack = []

        for p in s:
            # If we have a matching parenthesis, then we pop it
            # Otherwise we add it to the stack
            try:
                if ht[p] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(p)
            except:
                stack.append(p)

        return stack == []