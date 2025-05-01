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
    # Time complexity: O(2^(lenS + lenP))
    # Space complexity: O(lenS * lenP) where lenS and lenP are the len of s and p respectively
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

    # top-down dynamic programing with memoization based on recursion approach above
    # Time complexity: O(lenS * lenP)
    # Space complexity: O(lenS * lenP)
    def is_match_dp(self, s: str, p: str) -> bool:
        dp = {}

        def dfs(i: int, j: int) -> bool:
            if (i, j) in dp: return dp[(i, j)]
            # if i and j is out of bound, the initial string matches the pattern
            if i >= len(s) and j >= len(p):
                return True
            # if j is out of bound but i doesn't => the string doesn't match the pattern
            if j >= len(p): return False
            first_match = i < len(s) and p[j] in [s[i], '.']
            if j + 1 < len(p) and p[j + 1] == '*':
                # case 1: don't use the *
                # case 2: if first char is match, we can continue to check the remaining of string s
                # with pattern p
                dp[(i, j)] = dfs(i, j + 2) or (first_match and dfs(i + 1, j))
            else:
                dp[(i, j)] = first_match and dfs(i + 1, j + 1)
            return dp[(i, j)]

        return dfs(0, 0)


solution = Solution()
match = solution.is_match_dp("aa", "a*")
print(match)
