"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Constraints:
- 1 <= s.length <= 10^4
- s consists of parentheses only '()[]{}'.
"""


class Solution:
    # string, stack
    # time complexity: O(n)
    # space complexity: O(n)
    def is_valid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket in "([{":
                stack.append(bracket)
            else:
                # consider s as invalid if we did not found any opening brackets
                if not stack:
                    return False
                open = stack.pop()
                # if currently closing bracket is not match with opening bracket type,
                # we know s is not a valid string either
                if (
                        (bracket == ")" and open != "(")
                        or (bracket == "]" and open != "[")
                        or (bracket == "}" and open != "{")
                ):
                    return False
        return not len(stack)
