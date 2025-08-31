"""
Given a string s which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.

You may assume that the given expression is always valid.
All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings
as mathematical expressions, such as eval().

Constraints:
- 1 <= s.length <= 3 * 10^5
- s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
- s represents a valid expression.
- All the integers in the expression are non-negative integers in the range [0, 231 - 1].
- The answer is guaranteed to fit in a 32-bit integer.
"""
import math


class Solution:
    # stack, mathematics, string
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        stack, current_num = [], 0
        # make sure to pass the first number to the stack
        operation = '+'
        # remove leading and trailing whitespace for the special case inside the loop
        s = s.strip()
        for i, c in enumerate(s):
            if c == ' ':
                continue
            if c.isdigit():
                current_num = current_num * 10 + (ord(c) - ord('0'))
            if not c.isdigit() or i == len(s) - 1:
                # the expression is evaluated based on the precedence of the next operation
                # if the current operation is + or - => push to the stack
                if operation == '+':
                    stack.append(current_num)
                elif operation == '-':
                    stack.append(-current_num)
                # if operation is either * or /, the expression is evaluated
                # irrespective of the next operations
                elif operation == '*':
                    top = stack.pop()
                    stack.append(top * current_num)
                else:
                    top = stack.pop()
                    stack.append(math.trunc(top / current_num))
                current_num = 0
                operation = c
        result = 0
        while stack:
            top = stack.pop()
            result += top
        return result


solution = Solution()
print(solution.calculate("3+2*2"))
