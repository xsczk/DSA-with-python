"""
Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.


Example 1:
- Input: s = "()"
- Output: 1

Example 2:
- Input: s = "(())"
- Output: 2

Example 3:
- Input: s = "()()"
- Output: 2

Constraints:
- 2 <= s.length <= 50
- s consists of only '(' and ')'.
- s is a balanced parentheses string.
"""


class Solution:
    # array
    # time complexity: O(n)
    # space complexity: O(1) - array has maximum 30 elements
    def score_of_parentheses(self, s: str) -> int:
        # as the constraint tells us that s is a balanced parentheses string,
        # and s has maximum 50 characters, we initialize an array of length 30
        # which is the maximum number of balance parentheses can be formed
        res, i = 30 * [0], 0
        for c in s:
            if c == '(':
                i += 1
                # initialize new scope
                res[i] = 0
            else:
                i -= 1
                # calc outer scope based on inner scope's score
                res[i] += res[i + 1] + max(res[i + 1], 1)
        return res[0]
