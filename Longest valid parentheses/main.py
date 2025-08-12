"""
Given a string containing just the characters '(' and ')', return the length
of the longest valid (well-formed) parentheses substring.
A substring is a contiguous non-empty sequence of characters within a string.

Constraints:
- 0 <= s.length <= 3 * 10^4
- s[i] is '(', or ')'.
"""


class Solution:
    # stack
    # time complexity: O(n)
    # space complexity: O(n)
    def longest_valid_parentheses(self, s: str) -> int:
        max_len = 0
        stack = []
        # the position of the last invalid character which can't form a valid group of parentheses
        last_invalid = -1
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif stack:
                # found a valid open bracket
                stack.pop()
                # calculating the start position of the valid group
                start = stack[-1] + 1 if stack else last_invalid + 1
                max_len = max(max_len, i - start + 1)
            else:
                # update the stack to init state and last_invalid to i as we currently at the invalid position
                stack = []
                last_invalid = i
        return max_len

    # concise version base on the above logic
    def longest_valid_parentheses2(self, s: str) -> int:
        max_len = 0
        # initialize stack with -1 as a base for valid substring
        stack = [-1]
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                # if stack is not empty, calc the valid substring length
                if stack:
                    max_len = max(max_len, i - stack[-1])
                else:
                    # if stack is empty, push the cur index as new base
                    stack.append(i)
        return max_len
