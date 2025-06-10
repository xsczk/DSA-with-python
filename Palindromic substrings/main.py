"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

Constraints:
- 1 <= s.length <= 1000
- s consists of lowercase English letters.
"""


class Solution:
    # dynamic programing, memoization
    # time complexity: O(n^2)
    # space complexity: O(n^2) due to 2D-dp list
    def count_substrings(self, s: str) -> int:
        ans = 0
        if not s:
            return ans
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        # every single character is a palindrome
        for i in range(n):
            dp[i][i] = True
            ans += 1
        # check for substrings that have length >= 2
        for length in range(2, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1
                # if abc is a palindrome and x = y => xabcy is also a palindrome
                if s[start] == s[end] and (
                        dp[start + 1][end - 1] == True or length == 2):
                    dp[start][end] = True
                    ans += 1
        return ans

    # two pointers, expand from the beginning
    # time complexity: O(n^2)
    # space complexity: O(1)
    def count_substrings_2(self, s: str) -> int:
        ans = 0
        if not s:
            return ans

        def expand(i: int, j: int) -> int:
            num_of_substr = 0
            l, r = i, j
            while l >= 0 and r < len(s) and s[l] == s[r]:
                num_of_substr += 1
                l -= 1
                r += 1
            # return the total of palindromic substrings
            # can be formed with initial index i, j
            return num_of_substr

        for i in range(len(s)):
            # expand from substring that have odd length plus even length cases
            ans += expand(i, i) + expand(i, i + 1)
        return ans
