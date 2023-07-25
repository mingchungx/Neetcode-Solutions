class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        # Reverse Polish Notation is Postfix Operator
        # RPN(3, 4, +) => 7
        operations = "+-*/"
        # If we encounter an OPERATION, then we preform it on the top two and put that to the stack
        # If we encounter a NUMBER, then we add it to the stack
        stack = []

        for token in tokens:
            if token in operations:
                b = stack.pop()
                a = stack.pop()
                stack.append(int(eval(str(a) + token + str(b))))
            else:
                stack.append(token)

        return int(stack[0])