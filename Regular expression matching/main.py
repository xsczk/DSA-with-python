"""Given an input string s and a pattern p,
implement regular expression matching with support for '.' and '*' where:

- '.' Matches any single character.
- '*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Example 2:
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'.
Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
"""


class Solution:
    # recursion
    def is_match(self, s: str, p: str) -> bool:
        """
        :param s: text
        :param p: pattern
        """
        # base case
        if not p:
            return not s
        # checks whether the first character of the pattern matches the first character of the text
        first_match = bool(s) and p[0] in [s[0], '.']
        if len(p) >= 2 and p[1] == '*':
            # case 1: skip or not repeat the character before *
            # case 2: if first char is match, we can continue to check the remaining of string s
            # with pattern p
            return self.is_match(s, p[2:]) or (first_match and self.is_match(s[1:], p))
        else:
            # if first match and the next pattern is not *, continue to check remaining of both
            return first_match and self.is_match(s[1:], p[1:])


solution = Solution()
match = solution.is_match("aa", "a*")
print(match)