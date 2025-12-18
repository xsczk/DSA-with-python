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

    # two pointers
    # time complexity: O(n)
    # space complexity: O(1)
    def checkValidString2(self, s: str) -> bool:
        open_count = close_count = 0
        n = len(s)
        for i in range(n):
            # treat * as (
            if s[i] == '(' or s[i] == '*':
                open_count += 1
            else:
                open_count -= 1
                if open_count < 0: return False
            # treat * as )
            if s[n - i - 1] == '(':
                close_count -= 1
                if close_count < 0: return False
            else:
                close_count += 1
        return True
