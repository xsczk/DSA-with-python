"""
You are given an array of strings tokens that represents an arithmetic expression
in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:
- The valid operators are '+', '-', '*', and '/'.
- Each operand may be an integer or another expression.
- The division between two integers always truncates toward zero.
- There will not be any division by zero.
- The input represents a valid arithmetic expression in a reverse polish notation.
- The answer and all the intermediate calculations can be represented in a 32-bit integer.

Constraints:
- 1 <= tokens.length <= 104
- tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
"""


class Solution:
    # stack, simulation
    # time complexity: O(n)
    # space complexity: O(n)
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        expression = {"+", "-", "*", "/"}
        # for more detail and better explanation about RPN, check this resource
        # https://en.wikipedia.org/wiki/Reverse_Polish_notation
        for token in tokens:
            if token in expression:
                a, b = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(b + a)
                elif token == "-":
                    stack.append(b - a)
                elif token == "*":
                    stack.append(b * a)
                elif token == "/":
                    stack.append(int(b / a))
            else:
                stack.append(int(token))
        return stack[0]


solution = Solution()
print(solution.evalRPN(["4", "13", "5", "/", "+"]))
