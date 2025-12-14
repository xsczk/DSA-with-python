"""
Given a string s containing only three types of characters: '(', ')' and '*',
return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '('
or an empty string "".

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "(*)"
Output: true

Example 3:
Input: s = "(*))"
Output: true

Constraints:
- 1 <= s.length <= 100
- s[i] is '(', ')' or '*'.
"""


class Solution:
    # stack
    # time complexity: O(n)
    # space complexity: O(n)
    def check_valid_string(self, s: str) -> bool:
        # (((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())
        # [(((((((((((((]
        # [***************]
        asterisks = []
        open_brackets = []
        for i, char in enumerate(s):
            if char == '(':
                open_brackets.append(i)
            elif char == '*':
                asterisks.append(i)
            else:
                if open_brackets:
                    open_brackets.pop()
                # use * as (
                elif asterisks:
                    asterisks.pop()
                else:
                    return False
        # check and act the remaining asterisk as ),
        # but make sure each index of * comes after the corresponding (
        while open_brackets and asterisks:
            if open_brackets.pop() > asterisks.pop():
                return False
        return not open_brackets
